import{e as v,s as h,d as m,k,w as _,o as p,c as g,a as s,v as b,x as w,u as d,n as f,y as x,l as $,f as y,z as C,F as S}from"./vendor.3fc8d3f7.js";import{_ as B,u as M}from"./index.d0cd7b5e.js";function V(){const e=function(){return((1+Math.random())*65536|0).toString(16).substring(1)};return e()+e()+"-"+e()+"-"+e()+"-"+e()+"-"+e()+e()+e()}const D={class:"inline-block sw-switch",style:{"background-color":"transparent",color:"inherit"}},z=["for"],F={class:"relative"},N=["id","checked"],q=v({props:{big:{type:Boolean,default:!1},value:{type:Boolean,required:!0}},emits:["update:value"],setup(e,{emit:n}){const l=e,{value:u}=h(l),t=m(!1),r=V();function i(){n("update:value",t.value)}return k(()=>{t.value=u.value}),_(()=>l.value,(a,o)=>{t.value=a}),(a,o)=>(p(),g("div",D,[s("label",{for:"toggle"+d(r),class:"flex items-center cursor-pointer"},[s("div",F,[b(s("input",{id:"toggle"+d(r),type:"checkbox",class:"sr-only",checked:t.value,"onUpdate:modelValue":o[0]||(o[0]=c=>t.value=c),onChange:o[1]||(o[1]=c=>i())},null,40,N),[[w,t.value]]),s("div",{class:f(["block rounded-full bg",{big:e.big===!0}])},null,2),s("div",{class:f(["absolute transition rounded-full dot left-1 top-1",{big:e.big===!0}])},null,2)]),x(a.$slots,"default")],8,z)]))}}),E=v({components:{SwSwitch:q},setup(){return{user:M}}}),G=s("div",{class:"text-xl text-gray-500 w-max dark:text-gray-300"},"Settings",-1),R=s("div",{class:"ml-2"},"Mode sombre",-1);function U(e,n,l,u,t,r){const i=$("sw-switch");return p(),g(S,null,[G,y(i,{onChange:n[0]||(n[0]=a=>e.user.toggleDarkMode()),checked:e.user.isDarkMode.value,class:"mt-5 switch-secondary"},{default:C(()=>[R]),_:1},8,["checked"])],64)}var H=B(E,[["render",U]]);export{H as default};