/* Reuse LuCI's already-rendered port data. No request, polling timer or backend change. */
(function(){
 'use strict';
 if(!['admin-status','admin-status-overview'].includes(document.body.dataset.page))return;
 var view=document.getElementById('view'),deck=document.querySelector('.nk-portdeck');
 if(!view||!deck)return;
 var frame=0,last='';
 function update(){
  frame=0;var states=[];
  view.querySelectorAll('.ifacebox').forEach(function(box){
   var head=box.querySelector('.ifacebox-head'),body=box.querySelector('.ifacebox-body');
   var name=head&&head.textContent.trim();if(!/^lan[1-8]$/.test(name)||!body)return;
   var icon=body.querySelector('img[src*="/icons/port_"]');if(!icon)return;
   var up=/port_(?:pse_)?up\.svg/.test(icon.getAttribute('src'));
   var speed=body.textContent.trim().replace(/\s+/g,' ');
   states.push({name:name,up:up,speed:speed});
  });
  if(!states.length)return;
  var signature=JSON.stringify(states);if(signature===last)return;last=signature;
  states.forEach(function(s){var p=deck.querySelector('[data-port="'+s.name+'"]');if(!p)return;p.classList.toggle('is-up',s.up);p.querySelector('strong').textContent=s.up?s.speed:'—';p.querySelector('.nk-port-state').textContent=s.up?_('Connected'):_('no link');p.title=s.name+' · '+(s.up?s.speed:_('no link'));});
  document.getElementById('nk-active').textContent=states.filter(function(s){return s.up;}).length;
  deck.hidden=false;
 }
 new MutationObserver(function(){if(!frame)frame=requestAnimationFrame(update);}).observe(view,{childList:true,subtree:true,characterData:true});
 update();
})();
