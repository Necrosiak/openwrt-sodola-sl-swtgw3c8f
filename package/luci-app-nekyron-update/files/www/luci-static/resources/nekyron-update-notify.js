'use strict';
'require baseclass';
'require rpc';
'require ui';
var status=rpc.declare({object:'nekyron_update',method:'status',expect:{'':{}}});
var check=rpc.declare({object:'nekyron_update',method:'check',params:['force'],expect:{'':{}}});
return baseclass.extend({
 __init__:function(){
  var tries=0,shown=false;
  function notice(st){
   if(shown||!st.enabled||!st.latest||!['available','ready'].includes(st.state))return;
   shown=true;
   ui.addNotification(null,E('p',{},[
    _('A new Nekyron firmware is available:')+' '+st.latest.version+' ',
    E('a',{href:L.url('admin/system/nekyron-update'),'class':'cbi-button cbi-button-action'},_('View and update'))
   ]),'info');
  }
  function refresh(){return status().then(function(st){notice(st);if(!shown&&++tries<20&&['idle','checking'].includes(st.state))setTimeout(refresh,2000);}).catch(function(){});}
  status().then(notice).catch(function(){});
  check(false).then(function(){setTimeout(refresh,1200);}).catch(function(){});
 }
});
