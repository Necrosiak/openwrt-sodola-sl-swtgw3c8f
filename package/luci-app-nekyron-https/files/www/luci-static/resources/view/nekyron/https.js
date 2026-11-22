'use strict';
'require view';
'require rpc';
'require ui';
var status=rpc.declare({object:'nekyron_https',method:'status',expect:{'':{}}});
var update=rpc.declare({object:'nekyron_https',method:'update',expect:{'':{}}});
return view.extend({
 load:function(){return status();},
 render:function(st){
  var self=this;
  function row(label,text){return E('div',{'class':'cbi-value'},[E('label',{'class':'cbi-value-title'},label),E('div',{'class':'cbi-value-field'},text)]);}
  var download=E('button',{'class':'cbi-button cbi-button-neutral',disabled:!st.certificate,click:function(){
   var pem='-----BEGIN CERTIFICATE-----\n'+st.certificate.match(/.{1,64}/g).join('\n')+'\n-----END CERTIFICATE-----\n';
   var url=URL.createObjectURL(new Blob([pem],{type:'application/x-pem-file'}));
   var a=E('a',{href:url,download:'switch-https.crt'});document.body.appendChild(a);a.click();a.remove();setTimeout(function(){URL.revokeObjectURL(url);},1000);
  }},_('Download public certificate'));
  var renew=E('button',{'class':'cbi-button cbi-button-action',disabled:!L.hasViewPermission()||!st.managed||!st.clock_ready,click:ui.createHandlerFn(self,function(){
   ui.showModal(_('Update certificate'),[E('p',{},_('This generates a new certificate for this switch. HTTPS will restart briefly. Import the new public certificate into your browser afterwards.')),
    E('div',{'class':'right'},[E('button',{'class':'cbi-button',click:ui.hideModal},_('Cancel')),' ',E('button',{'class':'cbi-button cbi-button-action',click:ui.createHandlerFn(self,function(){return update().then(function(r){ui.hideModal();ui.addNotification(null,E('p',r.ok?_('Certificate updated. Reload this page and trust the new certificate.'):_('Certificate update unavailable. Check the clock and HTTPS configuration.')),r.ok?'info':'warning');});})},_('Update certificate'))])]);
  })},_('Update certificate'));
  return E('div',{'class':'cbi-map'},[
   E('h2',{},_('HTTPS Certificate')),
   E('p',{'class':'cbi-map-descr'},_('After firmware installation, a unique certificate is generated automatically once the device clock and its DHCP address are available. No private key is shared between switches.')),
   E('div',{'class':'cbi-section'},[
    row(_('Automatic generation'),st.managed?_('Enabled'):_('Disabled')),
    row(_('System clock'),st.clock_ready?_('Ready'):_('Waiting for time synchronization')),
    row(_('Generated'),st.issued?new Date(st.issued*1000).toLocaleString():_('Waiting for automatic generation')),
    row(_('Certificate names'),E('code',{},st.names||'—')),
    row(_('SHA-256 fingerprint'),E('code',{'style':'overflow-wrap:anywhere'},st.fingerprint||'—')),
    row(_('Actions'),E('div',{'style':'display:flex;flex-wrap:wrap;gap:8px'},[renew,download]))
   ]),
   E('p',{},_('The certificate encrypts access to this switch. Each administration computer must trust its public certificate to remove browser warnings. A new IP address or certificate renewal can require importing it again.'))
  ]);
 },
 handleSave:null,handleSaveApply:null,handleReset:null
});
