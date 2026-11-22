'use strict';
'require view';
'require rpc';
'require poll';
'require ui';
var status=rpc.declare({object:'nekyron_update',method:'status',expect:{'':{}}});
var check=rpc.declare({object:'nekyron_update',method:'check',params:['force'],expect:{'':{}}});
var action=rpc.declare({object:'nekyron_update',method:'action',params:['command','token','channel'],expect:{'':{}}});
return view.extend({
 load:function(){return status();},
 render:function(initial){
  var self=this,root=E('div'),latest=initial,readonly=!L.hasViewPermission();
  function row(label,content){return E('div',{'class':'cbi-value'},[E('label',{'class':'cbi-value-title'},label),E('div',{'class':'cbi-value-field'},Array.isArray(content)?content:[content])]);}
  function refresh(){return status().then(draw);}
  function run(command,token,channel){return action(command,token||'',channel||'').then(function(r){if(!r.ok)ui.addNotification(null,E('p',_('Unable to start this operation.')),'warning');return refresh();});}
  function draw(st){
   latest=st;
   var busy=['checking','staging','installing'].includes(st.state),m=st.latest||{},nodes=[];
   var states={idle:_('Not checked yet'),checking:_('Checking for updates…'),available:_('Update available'),current:_('No newer compatible signed firmware'),staging:_('Downloading and verifying…'),ready:_('Verified image ready to install'),installing:_('Installing and restarting…'),error:_('Update unavailable')};
   var errors={network:_('The update server is unreachable. Try again later.'),signature:_('The update signature is invalid.'),incompatible:_('This image does not match this switch and firmware profile.'),identity:_('The installed firmware profile cannot be identified safely.'),memory:_('Not enough available RAM to download this image safely.'),download:_('Firmware download failed.'),checksum:_('The downloaded image checksum does not match.'),validation:_('OpenWrt rejected the image. Installation is blocked.'),stale:_('The selected image changed. Check for updates again.'),disabled:_('Update checking is disabled.'),install:_('Unable to start firmware installation.')};
   nodes.push(E('h2',{},_('Nekyron firmware updates')));
   nodes.push(E('p',{'class':'cbi-map-descr'},_('Updates are checked when you sign in. Nothing is installed automatically. Only signed images for this exact board and profile are accepted.')));
   var box=E('div',{'class':'cbi-section'},[
    row(_('Installed version'),(st.current||{}).version||_('Unknown')),
    row(_('Profile'),(st.current||{}).flavor||_('Unknown')),
    row(_('Status'),states[st.state]||_('Unknown'))
   ]);
   if(st.error)box.appendChild(row(_('Details'),errors[st.error]||_('The update could not be checked.')));
   if(st.checked)box.appendChild(row(_('Last check'),new Date(st.checked*1000).toLocaleString()));
   if(m.version){
    box.appendChild(row(_('Available version'),m.version));
    box.appendChild(row(_('Release notes'),E('a',{href:'https://github.com/Necrosiak/openwrt-sodola-sl-swtgw3c8f/releases/tag/'+encodeURIComponent(m.tag),target:'_blank',rel:'noopener noreferrer'},_('Read release notes'))));
    if(m.channel==='candidate')box.appendChild(row(_('Channel'),_('Experimental candidate — not hardware validated')));
   }
   var buttons=[E('button',{'class':'cbi-button cbi-button-action',disabled:busy,click:ui.createHandlerFn(self,function(){return check(true).then(function(){return new Promise(function(resolve){setTimeout(resolve,800);});}).then(refresh);})},_('Check now'))];
   if(st.state==='available')buttons.push(E('button',{'class':'cbi-button cbi-button-positive',disabled:readonly||busy,click:ui.createHandlerFn(self,function(){return run('stage',m.sha256);})},_('Download and verify update')));
   if(st.state==='ready')buttons.push(E('button',{'class':'cbi-button cbi-button-positive',disabled:readonly,click:function(){
    ui.showModal(_('Install firmware update'),[
     E('p',{},_('The switch will restart and network connections will be interrupted. Settings and passwords are retained. Keep the power connected throughout the update.')),
     E('p',{},_('Extra packages may need reinstalling. HTTPS will regenerate after NTP synchronization; your browser may ask you to trust the new certificate.')),
     E('p',{},m.version),
     m.channel==='candidate'?E('p',{},_('This is an experimental candidate that has not been validated on hardware.')):E('span'),
     E('div',{'class':'right'},[E('button',{'class':'cbi-button',click:ui.hideModal},_('Cancel')),' ',E('button',{'class':'cbi-button cbi-button-positive',click:ui.createHandlerFn(self,function(){
      return action('install',m.sha256,'').then(function(r){if(!r.ok){ui.hideModal();ui.addNotification(null,E('p',_('Unable to start this operation.')),'warning');return;}ui.showModal(_('Installing and restarting…'),[E('p',{'class':'spinning'},_('Wait for the switch to restart. Do not disconnect the power.'))]);ui.awaitReconnect(window.location.hostname);});
     })},_('Install and restart'))])
    ]);
   }},_('Install update')));
   if(!readonly)buttons.push(E('button',{'class':'cbi-button cbi-button-neutral',click:function(ev){var f=E('form',{method:'post',action:L.env.cgi_base+'/cgi-backup',enctype:'application/x-www-form-urlencoded'},E('input',{type:'hidden',name:'sessionid',value:rpc.getSessionID()}));document.body.appendChild(f);f.submit();f.remove();}},_('Download configuration backup')));
   box.appendChild(row(_('Actions'),E('div',{'style':'display:flex;flex-wrap:wrap;gap:8px'},buttons)));nodes.push(box);
   var channel=E('select',{disabled:readonly||busy,change:ui.createHandlerFn(self,function(ev){return run('channel','',ev.target.value);})},[
    E('option',{value:'release'},_('Published versions')),
    E('option',{value:'candidate'},_('Include automatic experimental candidates'))
   ]);channel.value=st.channel||'release';
   nodes.push(E('div',{'class':'cbi-section'},[row(_('Update channel'),channel),E('p',{'style':'padding:0 20px 16px'},_('Automatic candidates can contain upstream security fixes and functional changes. Successful compilation is not hardware validation. Installation always requires confirmation.'))]));
   root.replaceChildren.apply(root,nodes);
  }
  draw(initial);
  poll.add(function(){return status().then(function(st){if(JSON.stringify(st)!==JSON.stringify(latest)&&!(root.contains(document.activeElement)&&/^(SELECT|INPUT)$/.test(document.activeElement.tagName)))draw(st);});},3);
  return root;
 },
 handleSave:null,handleSaveApply:null,handleReset:null
});
