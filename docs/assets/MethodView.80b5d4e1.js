import{r as xe,d as ot}from"./index.50890cf2.js";import{d as ke,r as K,D as Le,o as O,c as k,a as M,h as G,F as Be,k as lt,e as ve,j as ct,E as dt,t as ut,b as Se}from"./vendor.f90edea8.js";import ft from"./DsCodeBlock.30a9015d.js";var ce={exports:{}};function de(e){return e instanceof Map?e.clear=e.delete=e.set=function(){throw new Error("map is read-only")}:e instanceof Set&&(e.add=e.clear=e.delete=function(){throw new Error("set is read-only")}),Object.freeze(e),Object.getOwnPropertyNames(e).forEach(function(t){var n=e[t];typeof n=="object"&&!Object.isFrozen(n)&&de(n)}),e}ce.exports=de;ce.exports.default=de;class Me{constructor(t){t.data===void 0&&(t.data={}),this.data=t.data,this.isMatchIgnored=!1}ignoreMatch(){this.isMatchIgnored=!0}}function Ie(e){return e.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;")}function P(e,...t){const n=Object.create(null);for(const d in e)n[d]=e[d];return t.forEach(function(d){for(const w in d)n[w]=d[w]}),n}const pt="</span>",Re=e=>!!e.scope||e.sublanguage&&e.language,ht=(e,{prefix:t})=>{if(e.includes(".")){const n=e.split(".");return[`${t}${n.shift()}`,...n.map((d,w)=>`${d}${"_".repeat(w+1)}`)].join(" ")}return`${t}${e}`};class gt{constructor(t,n){this.buffer="",this.classPrefix=n.classPrefix,t.walk(this)}addText(t){this.buffer+=Ie(t)}openNode(t){if(!Re(t))return;let n="";t.sublanguage?n=`language-${t.language}`:n=ht(t.scope,{prefix:this.classPrefix}),this.span(n)}closeNode(t){!Re(t)||(this.buffer+=pt)}value(){return this.buffer}span(t){this.buffer+=`<span class="${t}">`}}const Ae=(e={})=>{const t={children:[]};return Object.assign(t,e),t};class ue{constructor(){this.rootNode=Ae(),this.stack=[this.rootNode]}get top(){return this.stack[this.stack.length-1]}get root(){return this.rootNode}add(t){this.top.children.push(t)}openNode(t){const n=Ae({scope:t});this.add(n),this.stack.push(n)}closeNode(){if(this.stack.length>1)return this.stack.pop()}closeAllNodes(){for(;this.closeNode(););}toJSON(){return JSON.stringify(this.rootNode,null,4)}walk(t){return this.constructor._walk(t,this.rootNode)}static _walk(t,n){return typeof n=="string"?t.addText(n):n.children&&(t.openNode(n),n.children.forEach(d=>this._walk(t,d)),t.closeNode(n)),t}static _collapse(t){typeof t!="string"&&(!t.children||(t.children.every(n=>typeof n=="string")?t.children=[t.children.join("")]:t.children.forEach(n=>{ue._collapse(n)})))}}class _t extends ue{constructor(t){super(),this.options=t}addKeyword(t,n){t!==""&&(this.openNode(n),this.addText(t),this.closeNode())}addText(t){t!==""&&this.add(t)}addSublanguage(t,n){const d=t.root;d.sublanguage=!0,d.language=n,this.add(d)}toHTML(){return new gt(this,this.options).value()}finalize(){return!0}}function z(e){return e?typeof e=="string"?e:e.source:null}function Fe(e){return U("(?=",e,")")}function mt(e){return U("(?:",e,")*")}function bt(e){return U("(?:",e,")?")}function U(...e){return e.map(n=>z(n)).join("")}function wt(e){const t=e[e.length-1];return typeof t=="object"&&t.constructor===Object?(e.splice(e.length-1,1),t):{}}function fe(...e){const t=wt(e);return"("+(t.capture?"":"?:")+e.map(d=>z(d)).join("|")+")"}function He(e){return new RegExp(e.toString()+"|").exec("").length-1}function yt(e,t){const n=e&&e.exec(t);return n&&n.index===0}const Et=/\[(?:[^\\\]]|\\.)*\]|\(\??|\\([1-9][0-9]*)|\\./;function pe(e,{joinWith:t}){let n=0;return e.map(d=>{n+=1;const w=n;let m=z(d),r="";for(;m.length>0;){const a=Et.exec(m);if(!a){r+=m;break}r+=m.substring(0,a.index),m=m.substring(a.index+a[0].length),a[0][0]==="\\"&&a[1]?r+="\\"+String(Number(a[1])+w):(r+=a[0],a[0]==="("&&n++)}return r}).map(d=>`(${d})`).join(t)}const xt=/\b\B/,Pe="[a-zA-Z]\\w*",he="[a-zA-Z_]\\w*",je="\\b\\d+(\\.\\d+)?",$e="(-?)(\\b0[xX][a-fA-F0-9]+|(\\b\\d+(\\.\\d*)?|\\.\\d+)([eE][-+]?\\d+)?)",Ue="\\b(0b[01]+)",vt="!|!=|!==|%|%=|&|&&|&=|\\*|\\*=|\\+|\\+=|,|-|-=|/=|/|:|;|<<|<<=|<=|<|===|==|=|>>>=|>>=|>=|>>>|>>|>|\\?|\\[|\\{|\\(|\\^|\\^=|\\||\\|=|\\|\\||~",St=(e={})=>{const t=/^#![ ]*\//;return e.binary&&(e.begin=U(t,/.*\b/,e.binary,/\b.*/)),P({scope:"meta",begin:t,end:/$/,relevance:0,"on:begin":(n,d)=>{n.index!==0&&d.ignoreMatch()}},e)},Q={begin:"\\\\[\\s\\S]",relevance:0},Mt={scope:"string",begin:"'",end:"'",illegal:"\\n",contains:[Q]},Rt={scope:"string",begin:'"',end:'"',illegal:"\\n",contains:[Q]},At={begin:/\b(a|an|the|are|I'm|isn't|don't|doesn't|won't|but|just|should|pretty|simply|enough|gonna|going|wtf|so|such|will|you|your|they|like|more)\b/},se=function(e,t,n={}){const d=P({scope:"comment",begin:e,end:t,contains:[]},n);d.contains.push({scope:"doctag",begin:"[ ]*(?=(TODO|FIXME|NOTE|BUG|OPTIMIZE|HACK|XXX):)",end:/(TODO|FIXME|NOTE|BUG|OPTIMIZE|HACK|XXX):/,excludeBegin:!0,relevance:0});const w=fe("I","a","is","so","us","to","at","if","in","it","on",/[A-Za-z]+['](d|ve|re|ll|t|s|n)/,/[A-Za-z]+[-][a-z]+/,/[A-Za-z][a-z]{2,}/);return d.contains.push({begin:U(/[ ]+/,"(",w,/[.]?[:]?([.][ ]|[ ])/,"){3}")}),d},Tt=se("//","$"),Ct=se("/\\*","\\*/"),Dt=se("#","$"),Nt={scope:"number",begin:je,relevance:0},Ot={scope:"number",begin:$e,relevance:0},kt={scope:"number",begin:Ue,relevance:0},Lt={begin:/(?=\/[^/\n]*\/)/,contains:[{scope:"regexp",begin:/\//,end:/\/[gimuy]*/,illegal:/\n/,contains:[Q,{begin:/\[/,end:/\]/,relevance:0,contains:[Q]}]}]},Bt={scope:"title",begin:Pe,relevance:0},It={scope:"title",begin:he,relevance:0},Ft={begin:"\\.\\s*"+he,relevance:0},Ht=function(e){return Object.assign(e,{"on:begin":(t,n)=>{n.data._beginMatch=t[1]},"on:end":(t,n)=>{n.data._beginMatch!==t[1]&&n.ignoreMatch()}})};var te=Object.freeze({__proto__:null,MATCH_NOTHING_RE:xt,IDENT_RE:Pe,UNDERSCORE_IDENT_RE:he,NUMBER_RE:je,C_NUMBER_RE:$e,BINARY_NUMBER_RE:Ue,RE_STARTERS_RE:vt,SHEBANG:St,BACKSLASH_ESCAPE:Q,APOS_STRING_MODE:Mt,QUOTE_STRING_MODE:Rt,PHRASAL_WORDS_MODE:At,COMMENT:se,C_LINE_COMMENT_MODE:Tt,C_BLOCK_COMMENT_MODE:Ct,HASH_COMMENT_MODE:Dt,NUMBER_MODE:Nt,C_NUMBER_MODE:Ot,BINARY_NUMBER_MODE:kt,REGEXP_MODE:Lt,TITLE_MODE:Bt,UNDERSCORE_TITLE_MODE:It,METHOD_GUARD:Ft,END_SAME_AS_BEGIN:Ht});function Pt(e,t){e.input[e.index-1]==="."&&t.ignoreMatch()}function jt(e,t){e.className!==void 0&&(e.scope=e.className,delete e.className)}function $t(e,t){!t||!e.beginKeywords||(e.begin="\\b("+e.beginKeywords.split(" ").join("|")+")(?!\\.)(?=\\b|\\s)",e.__beforeBegin=Pt,e.keywords=e.keywords||e.beginKeywords,delete e.beginKeywords,e.relevance===void 0&&(e.relevance=0))}function Ut(e,t){!Array.isArray(e.illegal)||(e.illegal=fe(...e.illegal))}function qt(e,t){if(!!e.match){if(e.begin||e.end)throw new Error("begin & end are not supported with match");e.begin=e.match,delete e.match}}function Kt(e,t){e.relevance===void 0&&(e.relevance=1)}const Gt=(e,t)=>{if(!e.beforeMatch)return;if(e.starts)throw new Error("beforeMatch cannot be used with starts");const n=Object.assign({},e);Object.keys(e).forEach(d=>{delete e[d]}),e.keywords=n.keywords,e.begin=U(n.beforeMatch,Fe(n.begin)),e.starts={relevance:0,contains:[Object.assign(n,{endsParent:!0})]},e.relevance=0,delete n.beforeMatch},zt=["of","and","for","in","not","or","if","then","parent","list","value"],Qt="keyword";function qe(e,t,n=Qt){const d=Object.create(null);return typeof e=="string"?w(n,e.split(" ")):Array.isArray(e)?w(n,e):Object.keys(e).forEach(function(m){Object.assign(d,qe(e[m],t,m))}),d;function w(m,r){t&&(r=r.map(a=>a.toLowerCase())),r.forEach(function(a){const o=a.split("|");d[o[0]]=[m,Wt(o[0],o[1])]})}}function Wt(e,t){return t?Number(t):Xt(e)?0:1}function Xt(e){return zt.includes(e.toLowerCase())}const Te={},$=e=>{console.error(e)},Ce=(e,...t)=>{console.log(`WARN: ${e}`,...t)},q=(e,t)=>{Te[`${e}/${t}`]||(console.log(`Deprecated as of ${e}. ${t}`),Te[`${e}/${t}`]=!0)},ne=new Error;function Ke(e,t,{key:n}){let d=0;const w=e[n],m={},r={};for(let a=1;a<=t.length;a++)r[a+d]=w[a],m[a+d]=!0,d+=He(t[a-1]);e[n]=r,e[n]._emit=m,e[n]._multi=!0}function Yt(e){if(!!Array.isArray(e.begin)){if(e.skip||e.excludeBegin||e.returnBegin)throw $("skip, excludeBegin, returnBegin not compatible with beginScope: {}"),ne;if(typeof e.beginScope!="object"||e.beginScope===null)throw $("beginScope must be object"),ne;Ke(e,e.begin,{key:"beginScope"}),e.begin=pe(e.begin,{joinWith:""})}}function Vt(e){if(!!Array.isArray(e.end)){if(e.skip||e.excludeEnd||e.returnEnd)throw $("skip, excludeEnd, returnEnd not compatible with endScope: {}"),ne;if(typeof e.endScope!="object"||e.endScope===null)throw $("endScope must be object"),ne;Ke(e,e.end,{key:"endScope"}),e.end=pe(e.end,{joinWith:""})}}function Jt(e){e.scope&&typeof e.scope=="object"&&e.scope!==null&&(e.beginScope=e.scope,delete e.scope)}function Zt(e){Jt(e),typeof e.beginScope=="string"&&(e.beginScope={_wrap:e.beginScope}),typeof e.endScope=="string"&&(e.endScope={_wrap:e.endScope}),Yt(e),Vt(e)}function en(e){function t(r,a){return new RegExp(z(r),"m"+(e.case_insensitive?"i":"")+(e.unicodeRegex?"u":"")+(a?"g":""))}class n{constructor(){this.matchIndexes={},this.regexes=[],this.matchAt=1,this.position=0}addRule(a,o){o.position=this.position++,this.matchIndexes[this.matchAt]=o,this.regexes.push([o,a]),this.matchAt+=He(a)+1}compile(){this.regexes.length===0&&(this.exec=()=>null);const a=this.regexes.map(o=>o[1]);this.matcherRe=t(pe(a,{joinWith:"|"}),!0),this.lastIndex=0}exec(a){this.matcherRe.lastIndex=this.lastIndex;const o=this.matcherRe.exec(a);if(!o)return null;const h=o.findIndex((S,R)=>R>0&&S!==void 0),_=this.matchIndexes[h];return o.splice(0,h),Object.assign(o,_)}}class d{constructor(){this.rules=[],this.multiRegexes=[],this.count=0,this.lastIndex=0,this.regexIndex=0}getMatcher(a){if(this.multiRegexes[a])return this.multiRegexes[a];const o=new n;return this.rules.slice(a).forEach(([h,_])=>o.addRule(h,_)),o.compile(),this.multiRegexes[a]=o,o}resumingScanAtSamePosition(){return this.regexIndex!==0}considerAll(){this.regexIndex=0}addRule(a,o){this.rules.push([a,o]),o.type==="begin"&&this.count++}exec(a){const o=this.getMatcher(this.regexIndex);o.lastIndex=this.lastIndex;let h=o.exec(a);if(this.resumingScanAtSamePosition()&&!(h&&h.index===this.lastIndex)){const _=this.getMatcher(0);_.lastIndex=this.lastIndex+1,h=_.exec(a)}return h&&(this.regexIndex+=h.position+1,this.regexIndex===this.count&&this.considerAll()),h}}function w(r){const a=new d;return r.contains.forEach(o=>a.addRule(o.begin,{rule:o,type:"begin"})),r.terminatorEnd&&a.addRule(r.terminatorEnd,{type:"end"}),r.illegal&&a.addRule(r.illegal,{type:"illegal"}),a}function m(r,a){const o=r;if(r.isCompiled)return o;[jt,qt,Zt,Gt].forEach(_=>_(r,a)),e.compilerExtensions.forEach(_=>_(r,a)),r.__beforeBegin=null,[$t,Ut,Kt].forEach(_=>_(r,a)),r.isCompiled=!0;let h=null;return typeof r.keywords=="object"&&r.keywords.$pattern&&(r.keywords=Object.assign({},r.keywords),h=r.keywords.$pattern,delete r.keywords.$pattern),h=h||/\w+/,r.keywords&&(r.keywords=qe(r.keywords,e.case_insensitive)),o.keywordPatternRe=t(h,!0),a&&(r.begin||(r.begin=/\B|\b/),o.beginRe=t(o.begin),!r.end&&!r.endsWithParent&&(r.end=/\B|\b/),r.end&&(o.endRe=t(o.end)),o.terminatorEnd=z(o.end)||"",r.endsWithParent&&a.terminatorEnd&&(o.terminatorEnd+=(r.end?"|":"")+a.terminatorEnd)),r.illegal&&(o.illegalRe=t(r.illegal)),r.contains||(r.contains=[]),r.contains=[].concat(...r.contains.map(function(_){return tn(_==="self"?r:_)})),r.contains.forEach(function(_){m(_,o)}),r.starts&&m(r.starts,a),o.matcher=w(o),o}if(e.compilerExtensions||(e.compilerExtensions=[]),e.contains&&e.contains.includes("self"))throw new Error("ERR: contains `self` is not supported at the top-level of a language.  See documentation.");return e.classNameAliases=P(e.classNameAliases||{}),m(e)}function Ge(e){return e?e.endsWithParent||Ge(e.starts):!1}function tn(e){return e.variants&&!e.cachedVariants&&(e.cachedVariants=e.variants.map(function(t){return P(e,{variants:null},t)})),e.cachedVariants?e.cachedVariants:Ge(e)?P(e,{starts:e.starts?P(e.starts):null}):Object.isFrozen(e)?P(e):e}var nn="11.7.0";class sn extends Error{constructor(t,n){super(t),this.name="HTMLInjectionError",this.html=n}}const le=Ie,De=P,Ne=Symbol("nomatch"),an=7,rn=function(e){const t=Object.create(null),n=Object.create(null),d=[];let w=!0;const m="Could not find the language '{}', did you forget to load/include a language module?",r={disableAutodetect:!0,name:"Plain text",contains:[]};let a={ignoreUnescapedHTML:!1,throwUnescapedHTML:!1,noHighlightRe:/^(no-?highlight)$/i,languageDetectRe:/\blang(?:uage)?-([\w-]+)\b/i,classPrefix:"hljs-",cssSelector:"pre code",languages:null,__emitter:_t};function o(s){return a.noHighlightRe.test(s)}function h(s){let c=s.className+" ";c+=s.parentNode?s.parentNode.className:"";const p=a.languageDetectRe.exec(c);if(p){const b=B(p[1]);return b||(Ce(m.replace("{}",p[1])),Ce("Falling back to no-highlight mode for this block.",s)),b?p[1]:"no-highlight"}return c.split(/\s+/).find(b=>o(b)||B(b))}function _(s,c,p){let b="",E="";typeof c=="object"?(b=s,p=c.ignoreIllegals,E=c.language):(q("10.7.0","highlight(lang, code, ...args) has been deprecated."),q("10.7.0",`Please use highlight(code, options) instead.
https://github.com/highlightjs/highlight.js/issues/2277`),E=s,b=c),p===void 0&&(p=!0);const C={code:b,language:E};V("before:highlight",C);const I=C.result?C.result:S(C.language,C.code,p);return I.code=C.code,V("after:highlight",I),I}function S(s,c,p,b){const E=Object.create(null);function C(i,l){return i.keywords[l]}function I(){if(!u.keywords){x.addText(y);return}let i=0;u.keywordPatternRe.lastIndex=0;let l=u.keywordPatternRe.exec(y),f="";for(;l;){f+=y.substring(i,l.index);const g=H.case_insensitive?l[0].toLowerCase():l[0],v=C(u,g);if(v){const[N,it]=v;if(x.addText(f),f="",E[g]=(E[g]||0)+1,E[g]<=an&&(ee+=it),N.startsWith("_"))f+=l[0];else{const rt=H.classNameAliases[N]||N;x.addKeyword(l[0],rt)}}else f+=l[0];i=u.keywordPatternRe.lastIndex,l=u.keywordPatternRe.exec(y)}f+=y.substring(i),x.addText(f)}function J(){if(y==="")return;let i=null;if(typeof u.subLanguage=="string"){if(!t[u.subLanguage]){x.addText(y);return}i=S(u.subLanguage,y,!0,Ee[u.subLanguage]),Ee[u.subLanguage]=i._top}else i=D(y,u.subLanguage.length?u.subLanguage:null);u.relevance>0&&(ee+=i.relevance),x.addSublanguage(i._emitter,i.language)}function A(){u.subLanguage!=null?J():I(),y=""}function F(i,l){let f=1;const g=l.length-1;for(;f<=g;){if(!i._emit[f]){f++;continue}const v=H.classNameAliases[i[f]]||i[f],N=l[f];v?x.addKeyword(N,v):(y=N,I(),y=""),f++}}function be(i,l){return i.scope&&typeof i.scope=="string"&&x.openNode(H.classNameAliases[i.scope]||i.scope),i.beginScope&&(i.beginScope._wrap?(x.addKeyword(y,H.classNameAliases[i.beginScope._wrap]||i.beginScope._wrap),y=""):i.beginScope._multi&&(F(i.beginScope,l),y="")),u=Object.create(i,{parent:{value:u}}),u}function we(i,l,f){let g=yt(i.endRe,f);if(g){if(i["on:end"]){const v=new Me(i);i["on:end"](l,v),v.isMatchIgnored&&(g=!1)}if(g){for(;i.endsParent&&i.parent;)i=i.parent;return i}}if(i.endsWithParent)return we(i.parent,l,f)}function et(i){return u.matcher.regexIndex===0?(y+=i[0],1):(oe=!0,0)}function tt(i){const l=i[0],f=i.rule,g=new Me(f),v=[f.__beforeBegin,f["on:begin"]];for(const N of v)if(!!N&&(N(i,g),g.isMatchIgnored))return et(l);return f.skip?y+=l:(f.excludeBegin&&(y+=l),A(),!f.returnBegin&&!f.excludeBegin&&(y=l)),be(f,i),f.returnBegin?0:l.length}function nt(i){const l=i[0],f=c.substring(i.index),g=we(u,i,f);if(!g)return Ne;const v=u;u.endScope&&u.endScope._wrap?(A(),x.addKeyword(l,u.endScope._wrap)):u.endScope&&u.endScope._multi?(A(),F(u.endScope,i)):v.skip?y+=l:(v.returnEnd||v.excludeEnd||(y+=l),A(),v.excludeEnd&&(y=l));do u.scope&&x.closeNode(),!u.skip&&!u.subLanguage&&(ee+=u.relevance),u=u.parent;while(u!==g.parent);return g.starts&&be(g.starts,i),v.returnEnd?0:l.length}function st(){const i=[];for(let l=u;l!==H;l=l.parent)l.scope&&i.unshift(l.scope);i.forEach(l=>x.openNode(l))}let Z={};function ye(i,l){const f=l&&l[0];if(y+=i,f==null)return A(),0;if(Z.type==="begin"&&l.type==="end"&&Z.index===l.index&&f===""){if(y+=c.slice(l.index,l.index+1),!w){const g=new Error(`0 width match regex (${s})`);throw g.languageName=s,g.badRule=Z.rule,g}return 1}if(Z=l,l.type==="begin")return tt(l);if(l.type==="illegal"&&!p){const g=new Error('Illegal lexeme "'+f+'" for mode "'+(u.scope||"<unnamed>")+'"');throw g.mode=u,g}else if(l.type==="end"){const g=nt(l);if(g!==Ne)return g}if(l.type==="illegal"&&f==="")return 1;if(re>1e5&&re>l.index*3)throw new Error("potential infinite loop, way more iterations than matches");return y+=f,f.length}const H=B(s);if(!H)throw $(m.replace("{}",s)),new Error('Unknown language: "'+s+'"');const at=en(H);let ie="",u=b||at;const Ee={},x=new a.__emitter(a);st();let y="",ee=0,j=0,re=0,oe=!1;try{for(u.matcher.considerAll();;){re++,oe?oe=!1:u.matcher.considerAll(),u.matcher.lastIndex=j;const i=u.matcher.exec(c);if(!i)break;const l=c.substring(j,i.index),f=ye(l,i);j=i.index+f}return ye(c.substring(j)),x.closeAllNodes(),x.finalize(),ie=x.toHTML(),{language:s,value:ie,relevance:ee,illegal:!1,_emitter:x,_top:u}}catch(i){if(i.message&&i.message.includes("Illegal"))return{language:s,value:le(c),illegal:!0,relevance:0,_illegalBy:{message:i.message,index:j,context:c.slice(j-100,j+100),mode:i.mode,resultSoFar:ie},_emitter:x};if(w)return{language:s,value:le(c),illegal:!1,relevance:0,errorRaised:i,_emitter:x,_top:u};throw i}}function R(s){const c={value:le(s),illegal:!1,relevance:0,_top:r,_emitter:new a.__emitter(a)};return c._emitter.addText(s),c}function D(s,c){c=c||a.languages||Object.keys(t);const p=R(s),b=c.filter(B).filter(me).map(A=>S(A,s,!1));b.unshift(p);const E=b.sort((A,F)=>{if(A.relevance!==F.relevance)return F.relevance-A.relevance;if(A.language&&F.language){if(B(A.language).supersetOf===F.language)return 1;if(B(F.language).supersetOf===A.language)return-1}return 0}),[C,I]=E,J=C;return J.secondBest=I,J}function T(s,c,p){const b=c&&n[c]||p;s.classList.add("hljs"),s.classList.add(`language-${b}`)}function L(s){let c=null;const p=h(s);if(o(p))return;if(V("before:highlightElement",{el:s,language:p}),s.children.length>0&&(a.ignoreUnescapedHTML||(console.warn("One of your code blocks includes unescaped HTML. This is a potentially serious security risk."),console.warn("https://github.com/highlightjs/highlight.js/wiki/security"),console.warn("The element with unescaped HTML:"),console.warn(s)),a.throwUnescapedHTML))throw new sn("One of your code blocks includes unescaped HTML.",s.innerHTML);c=s;const b=c.textContent,E=p?_(b,{language:p,ignoreIllegals:!0}):D(b);s.innerHTML=E.value,T(s,p,E.language),s.result={language:E.language,re:E.relevance,relevance:E.relevance},E.secondBest&&(s.secondBest={language:E.secondBest.language,relevance:E.secondBest.relevance}),V("after:highlightElement",{el:s,result:E,text:b})}function ae(s){a=De(a,s)}const X=()=>{Y(),q("10.6.0","initHighlighting() deprecated.  Use highlightAll() now.")};function ze(){Y(),q("10.6.0","initHighlightingOnLoad() deprecated.  Use highlightAll() now.")}let ge=!1;function Y(){if(document.readyState==="loading"){ge=!0;return}document.querySelectorAll(a.cssSelector).forEach(L)}function Qe(){ge&&Y()}typeof window!="undefined"&&window.addEventListener&&window.addEventListener("DOMContentLoaded",Qe,!1);function We(s,c){let p=null;try{p=c(e)}catch(b){if($("Language definition for '{}' could not be registered.".replace("{}",s)),w)$(b);else throw b;p=r}p.name||(p.name=s),t[s]=p,p.rawDefinition=c.bind(null,e),p.aliases&&_e(p.aliases,{languageName:s})}function Xe(s){delete t[s];for(const c of Object.keys(n))n[c]===s&&delete n[c]}function Ye(){return Object.keys(t)}function B(s){return s=(s||"").toLowerCase(),t[s]||t[n[s]]}function _e(s,{languageName:c}){typeof s=="string"&&(s=[s]),s.forEach(p=>{n[p.toLowerCase()]=c})}function me(s){const c=B(s);return c&&!c.disableAutodetect}function Ve(s){s["before:highlightBlock"]&&!s["before:highlightElement"]&&(s["before:highlightElement"]=c=>{s["before:highlightBlock"](Object.assign({block:c.el},c))}),s["after:highlightBlock"]&&!s["after:highlightElement"]&&(s["after:highlightElement"]=c=>{s["after:highlightBlock"](Object.assign({block:c.el},c))})}function Je(s){Ve(s),d.push(s)}function V(s,c){const p=s;d.forEach(function(b){b[p]&&b[p](c)})}function Ze(s){return q("10.7.0","highlightBlock will be removed entirely in v12.0"),q("10.7.0","Please use highlightElement now."),L(s)}Object.assign(e,{highlight:_,highlightAuto:D,highlightAll:Y,highlightElement:L,highlightBlock:Ze,configure:ae,initHighlighting:X,initHighlightingOnLoad:ze,registerLanguage:We,unregisterLanguage:Xe,listLanguages:Ye,getLanguage:B,registerAliases:_e,autoDetection:me,inherit:De,addPlugin:Je}),e.debugMode=function(){w=!1},e.safeMode=function(){w=!0},e.versionString=nn,e.regex={concat:U,lookahead:Fe,either:fe,optional:bt,anyNumberOfTimes:mt};for(const s in te)typeof te[s]=="object"&&ce.exports(te[s]);return Object.assign(e,te),e};var W=rn({}),on=W;W.HighlightJS=W;W.default=W;var Oe=on;function ln(e){const t=e.regex,n=/[\p{XID_Start}_]\p{XID_Continue}*/u,d=["and","as","assert","async","await","break","case","class","continue","def","del","elif","else","except","finally","for","from","global","if","import","in","is","lambda","match","nonlocal|10","not","or","pass","raise","return","try","while","with","yield"],a={$pattern:/[A-Za-z]\w+|__\w+__/,keyword:d,built_in:["__import__","abs","all","any","ascii","bin","bool","breakpoint","bytearray","bytes","callable","chr","classmethod","compile","complex","delattr","dict","dir","divmod","enumerate","eval","exec","filter","float","format","frozenset","getattr","globals","hasattr","hash","help","hex","id","input","int","isinstance","issubclass","iter","len","list","locals","map","max","memoryview","min","next","object","oct","open","ord","pow","print","property","range","repr","reversed","round","set","setattr","slice","sorted","staticmethod","str","sum","super","tuple","type","vars","zip"],literal:["__debug__","Ellipsis","False","None","NotImplemented","True"],type:["Any","Callable","Coroutine","Dict","List","Literal","Generic","Optional","Sequence","Set","Tuple","Type","Union"]},o={className:"meta",begin:/^(>>>|\.\.\.) /},h={className:"subst",begin:/\{/,end:/\}/,keywords:a,illegal:/#/},_={begin:/\{\{/,relevance:0},S={className:"string",contains:[e.BACKSLASH_ESCAPE],variants:[{begin:/([uU]|[bB]|[rR]|[bB][rR]|[rR][bB])?'''/,end:/'''/,contains:[e.BACKSLASH_ESCAPE,o],relevance:10},{begin:/([uU]|[bB]|[rR]|[bB][rR]|[rR][bB])?"""/,end:/"""/,contains:[e.BACKSLASH_ESCAPE,o],relevance:10},{begin:/([fF][rR]|[rR][fF]|[fF])'''/,end:/'''/,contains:[e.BACKSLASH_ESCAPE,o,_,h]},{begin:/([fF][rR]|[rR][fF]|[fF])"""/,end:/"""/,contains:[e.BACKSLASH_ESCAPE,o,_,h]},{begin:/([uU]|[rR])'/,end:/'/,relevance:10},{begin:/([uU]|[rR])"/,end:/"/,relevance:10},{begin:/([bB]|[bB][rR]|[rR][bB])'/,end:/'/},{begin:/([bB]|[bB][rR]|[rR][bB])"/,end:/"/},{begin:/([fF][rR]|[rR][fF]|[fF])'/,end:/'/,contains:[e.BACKSLASH_ESCAPE,_,h]},{begin:/([fF][rR]|[rR][fF]|[fF])"/,end:/"/,contains:[e.BACKSLASH_ESCAPE,_,h]},e.APOS_STRING_MODE,e.QUOTE_STRING_MODE]},R="[0-9](_?[0-9])*",D=`(\\b(${R}))?\\.(${R})|\\b(${R})\\.`,T=`\\b|${d.join("|")}`,L={className:"number",relevance:0,variants:[{begin:`(\\b(${R})|(${D}))[eE][+-]?(${R})[jJ]?(?=${T})`},{begin:`(${D})[jJ]?`},{begin:`\\b([1-9](_?[0-9])*|0+(_?0)*)[lLjJ]?(?=${T})`},{begin:`\\b0[bB](_?[01])+[lL]?(?=${T})`},{begin:`\\b0[oO](_?[0-7])+[lL]?(?=${T})`},{begin:`\\b0[xX](_?[0-9a-fA-F])+[lL]?(?=${T})`},{begin:`\\b(${R})[jJ](?=${T})`}]},ae={className:"comment",begin:t.lookahead(/# type:/),end:/$/,keywords:a,contains:[{begin:/# type:/},{begin:/#/,end:/\b\B/,endsWithParent:!0}]},X={className:"params",variants:[{className:"",begin:/\(\s*\)/,skip:!0},{begin:/\(/,end:/\)/,excludeBegin:!0,excludeEnd:!0,keywords:a,contains:["self",o,L,S,e.HASH_COMMENT_MODE]}]};return h.contains=[S,L,o],{name:"Python",aliases:["py","gyp","ipython"],unicodeRegex:!0,keywords:a,illegal:/(<\/|->|\?)|=>/,contains:[o,L,{begin:/\bself\b/},{beginKeywords:"if",relevance:0},S,ae,e.HASH_COMMENT_MODE,{match:[/\bdef/,/\s+/,n],scope:{1:"keyword",3:"title.function"},contains:[X]},{variants:[{match:[/\bclass/,/\s+/,n,/\s*/,/\(\s*/,n,/\s*\)/]},{match:[/\bclass/,/\s+/,n]}],scope:{1:"keyword",3:"title.class",6:"title.class.inherited"}},{className:"meta",begin:/^[\t ]*@/,end:/(?=#)|$/,contains:[L,X,S]}]}}const cn={class:"p-3"},dn={class:"px-5 py-2 code-block dark:bg-neutral-700 bg-amber-50 w-max"},un=["innerHTML"],fn={class:"pl-5 mt-5"},pn=["innerHTML"],hn=["innerHTML"],gn={key:1,class:"mt-5"},_n=M("div",{class:"text-lg italic"},"Parameters",-1),mn={class:"pl-5 mt-3 space-y-2"},bn=["innerHTML"],wn=["innerHTML"],yn=["innerHTML"],En={key:2,class:"mt-5"},xn=M("div",{class:"text-lg italic"},"Return",-1),vn={class:"mt-3"},Sn=["innerHTML"],Mn=ke({__name:"MethodDoc",props:{method:{type:Object,required:!0}},setup(e){const t=e;Oe.registerLanguage("python",ln);const n=K("");function d(){n.value=Oe.highlight(t.method.docstring.funcdef,{language:"python"}).value}return Le(()=>d()),(w,m)=>(O(),k("div",cn,[M("pre",dn,[M("code",{innerHTML:n.value,style:{"white-space":"pre"}},null,8,un)]),M("div",fn,[M("div",{innerHTML:e.method.docstring.description},null,8,pn),e.method.docstring.long_description?(O(),k("div",{key:0,class:"mt-3",innerHTML:e.method.docstring.long_description},null,8,hn)):G("",!0),Object.keys(e.method.docstring.params).length>0?(O(),k("div",gn,[_n,M("ul",mn,[(O(!0),k(Be,null,lt(Object.keys(e.method.docstring.params),r=>(O(),k("li",null,[M("span",{class:"font-bold",innerHTML:r},null,8,bn),ve(": "),M("span",{class:"hljs-built_in",innerHTML:e.method.docstring.params[r].type},null,8,wn),ve(": "),M("span",{innerHTML:e.method.docstring.params[r].description},null,8,yn)]))),256))])])):G("",!0),e.method.docstring.return.type!=null?(O(),k("div",En,[xn,M("div",vn,[M("span",{class:"hljs-built_in",innerHTML:e.method.docstring.return.type},null,8,Sn)])])):G("",!0)])]))}}),Rn={funcdef:'def w(self, v: int) -> "AltairChart"',description:`Set the width of the chart
`,long_description:"",example:`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.line_().w(500)`,params:{v:{description:`value in pixels
`,type:`int
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},An={funcdef:'def h(self, v: int) -> "AltairChart"',description:`Set the height of the chart
`,long_description:"",example:`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.line_().h(200)`,params:{v:{description:`value in pixels
`,type:`int
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},Tn={funcdef:'def wh(self, w: int, h: int) -> "AltairChart"',description:`Set the width and height of a chart
`,long_description:"",example:`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.line_().wh(500, 200)`,params:{w:{description:`width value in pixels
`,type:`int
`,default:null},h:{description:`height value in pixels
`,type:`int
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},Cn={funcdef:'def mw(self, v: int) -> "AltairChart"',description:`Configure the default mark width
`,long_description:"",example:`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.bar_().mw(7)`,params:{v:{description:`width value in pixels
`,type:`int
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},Dn={funcdef:'def pw(self, v: int) -> "AltairChart"',description:`Configure the default point width
`,long_description:"",example:`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.point_().pw(25)`,params:{v:{description:`width value in pixels
`,type:`int
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},Nn={funcdef:'def color(self, v: str) -> "AltairChart"',description:`Configure the chart color
`,long_description:"",example:`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.area_().color("forestgreen")`,params:{v:{description:`the color value
`,type:`str
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},On={funcdef:'def opacity(self, v: Union[int, float]) -> "AltairChart"',description:`Configure the chart opacity
`,long_description:"",example:`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.point_().opacity(0.5)`,params:{v:{description:`the opacity value
`,type:`Union[int, float]
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},kn={funcdef:'def tooltip(self, v: Union[str, List[str]]) -> "AltairChart"',description:`Configure a tooltip on hover for some colums
`,long_description:`The tooltip shows up when the user cursor goes
over the datapoint on the chart
`,example:`ds = await load_dataset("sp500")
ds.point_("date:T", "price:Q").tooltip(["date","price"])`,params:{v:{description:`column or list of columns to use for the tooltip
`,type:`Union[str, List[str]]
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},Ln={funcdef:'def to(self, v: str) -> "AltairChart"',description:`Change the chart type for an existing chart (only for the Altair engine)
`,long_description:null,example:null,params:{v:{description:`the new chart type
`,type:`str
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},Bn={funcdef:'def rx(self, v=-45) -> "AltairChart"',description:`Rotate the chart x labels
`,long_description:null,example:null,params:{v:{description:`angle of rotation to use, defaults to -45
`,type:`int, optional
`,default:`-45
`}},raises:{},return:{name:null,type:`Chart
`}},In={funcdef:'def nox(self) -> "AltairChart"',description:`Remove the x axis labels
`,long_description:"",example:`ds = await load_dataset("timeserie")
ds.axis("date:T", "data:Q")
(ds.line_().nox() + ds.point_().nox())`,params:{},raises:{},return:{name:null,type:`Chart
`}},Fn={funcdef:'def noy(self) -> "AltairChart"',description:`Remove the y axis labels
`,long_description:"",example:`ds = await load_dataset("timeserie")
ds.axis("date:T", "data:Q")
(ds.line_().noy() + ds.point_().noy())`,params:{},raises:{},return:{name:null,type:`Chart
`}},Hn={funcdef:'def title(self, v: str) -> "AltairChart"',description:`Add a text title to the chart
`,long_description:"",example:`ds = await load_dataset("timeserie")
ds.area_("date:T", "data:Q").title("The chart title")`,params:{v:{description:`the title text
`,type:`str
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},Pn={funcdef:'def colormap(self, column: str, **kwargs) -> "AltairChart"',description:`Add a values based colormap to the chart
`,long_description:null,example:null,params:{column:{description:`the column to use
`,type:`str
`,default:null},kwargs:{description:`the colors and values map to use
`,type:`Dict[str,str]
`,default:null}},raises:{ArgumentError:"raised if less than two colors are provided"},return:{name:null,type:`Chart
`}},jn={funcdef:'def qcolormap(self, column: str, **kwargs) -> "AltairChart"',description:`Add a quantiles based colormap to the chart
`,long_description:null,example:null,params:{column:{description:`the column to use
`,type:`str
`,default:null},kwargs:{description:`the colors and values map to use
`,type:`Dict[str,str]
`,default:null}},raises:{ArgumentError:"raised if less than two colors are provided"},return:{name:null,type:`Chart
`}},$n={funcdef:"def save_img(self, path: str)",description:`Save the chart to a png image
`,long_description:null,example:null,params:{path:{description:`the filepath
`,type:`str
`,default:null}},raises:{},return:{name:"",type:""}},Un={funcdef:"def get_html_(self) -> str",description:`Get html for an Altair chart
`,long_description:null,example:null,params:{},raises:{},return:{name:"",type:""}},qn={funcdef:"def html_header_()",description:`Returns html script tags for Altair
`,long_description:null,example:null,params:{},raises:{},return:{name:"",type:""}};var Kn={w:Rn,h:An,wh:Tn,mw:Cn,pw:Dn,color:Nn,opacity:On,tooltip:kn,to:Ln,rx:Bn,nox:In,noy:Fn,title:Hn,colormap:Pn,qcolormap:jn,save_img:$n,get_html_:Un,html_header_:qn};const Gn={funcdef:"def _load_csv(url, **kwargs) -> pd.DataFrame",description:null,long_description:null,example:null,params:{},raises:{},return:{name:"",type:""}},zn={funcdef:"def _load_django(query) -> pd.DataFrame",description:null,long_description:null,example:null,params:{},raises:{},return:{name:"",type:""}},Qn={funcdef:"def from_df(df: pd.DataFrame) -> DataSpace",description:`Intialize a DataSpace from a pandas DataFrame
`,long_description:null,example:null,params:{df:{description:`a pandas <tt class="docutils literal">DataFrame</tt>
`,type:null,default:null}},raises:{},return:{name:null,type:`<tt class="docutils literal">DataSpace</tt>
`}},Wn={funcdef:"def from_csv(url, **kwargs) -> DataSpace",description:`Loads csv data in the main dataframe
`,long_description:null,example:null,params:{url:{description:`url of the csv file to load:
can be absolute if it starts with <tt class="docutils literal">/</tt>
or relative if it starts with <tt class="docutils literal">./</tt>
`,type:`<tt class="docutils literal">str</tt>
`,default:null},kwargs:{description:`keyword arguments to pass to Pandas
<tt class="docutils literal">read_csv</tt> function
`,type:null,default:null}},raises:{},return:{name:null,type:`<tt class="docutils literal">DataSpace</tt>
`}},Xn={funcdef:"def from_django(query) -> DataSpace",description:`Load the main dataframe from a django orm query
`,long_description:null,example:null,params:{query:{description:`django query from a model
`,type:`django query
`,default:null}},raises:{},return:{name:null,type:`<tt class="docutils literal">DataSpace</tt>
`}};var Yn={_load_csv:Gn,_load_django:zn,from_df:Qn,from_csv:Wn,from_django:Xn};const Vn="return dataspace.from_df([1])",Jn=`ds = await load_dataset("bitcoin")
ds.show()`,Zn=`ds = await load_dataset("bitcoin")
print(ds.cols_())
ds.show()`,es=`data = {"col1": [1, np.nan, 2, None, 3, 3]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
n = ds.count_null_("col1")
print("The column has", n, "nulls")
ds.show()`,ts=`data = {"col1": ["foo", "", "bar", ""]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
n = ds.count_empty_("col1")
print("The column has", n, "empty values")
ds.show()`,ns=`data = {"col1": [0, 1, 2, 0, 3, 3]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
n = ds.count_zero_("col1")
print("The column has", n, "zero values")
ds.show()`,ss=`data = {"col1": [1, 2, 2, 3, 3, 3]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
n = ds.count_unique_("col1")
print("The column has", n, "unique values")
ds.show()`,as=`data = {"col1": ["one", "two", "two", "three", "three", "three"]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
df = ds.wunique_("col1")
print("Dataframe of unique values weights:")
print(df)`,is=`df = pd.DataFrame(np.linspace(1, 100, 1000))
ds = dataspace.from_df(df)
print("Initial length:", len(ds.df.index))
ds.limit(10)
print("New length after limiting:", len(ds.df.index))
ds.show()`,rs=`data = {"col1": ["A", "B", "C", "A", "B"]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
uv = ds.unique_("col1")
print("Colum unique values:", uv)
ds.show()`,os=`data = {"col1": [14, 8, np.nan], "col2": [2, np.nan, np.nan]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
print("The col1 has", ds.count_null_("col1"), "nulls")
ds.drop_nan("col1")
ds.show()`,ls=`data = {"col1": [14, 8, np.nan], "col2": [2, np.nan, np.nan]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.count_null_("col1")
ds.fill_nan("val", "col1")
ds.show()`,cs=`data = {"col1": np.array([1, None, ""]), "col2": np.array([None, 0, None])}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.count_empty_("col1")
ds.count_null_("col1")
ds.fill_nulls()
ds.show()`,ds=`ds = await load_dataset("timeserie")
print(ds.df.head())
ds.fdate("date", precision="D")
ds.show()`,us=`ds = await load_dataset("bitcoin")
print("1. Initial dataframe:")
print(ds.df.head(1))
print("2. Colums:")
print(ds.cols_())
ds.to_date("ReceiptTS")
print("3. New column types:", ds.cols_())
ds.show()`,fs=`ds = await load_dataset("timeserie")
print(ds.df.head())
ds.timestamps("date")
ds.show()`,ps=`data = {"col1": ["5", "8", "3"], "col2": ["8", "7", "2"]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
print("Column types:", ds.cols_())
ds.to_int("col1", "col2")
print("Column types after convert:", ds.cols_())
ds.show()`,hs=`data = {"col1": ["0.25", "0.85", "0.58"]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
print("Column types:", ds.cols_())
ds.to_float("col1")
print("Column types after convert:", ds.cols_())
ds.show()`,gs=`data = {"col1": [1, 0, 0]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
print("Column types:", ds.cols_())
ds.to_type(bool, "col1")
print("Column types after convert:", ds.cols_())
ds.show()`,_s=`data = {"col1": [" one ", "two "]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
print(list(ds.df.col1))
ds.strip("col1")
print(list(ds.df.col1))
ds.show()`,ms=`data = {"col1 ": [1, 2], " col2 ": [3, 4]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
print(list(ds.df.columns.values))
ds.strip_cols()
print(list(ds.df.columns.values))
ds.show()`,bs=`data = {"col1": [1.25889, 1.25874, 1.42587]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.roundvals("col1")
ds.show()`,ws=`data = {"col1": ["a", "b", "novalue"]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.replace("col1", "novalue", "c")
ds.show()`,ys=`data = {"col1": ["a", "b", "c"], "col2": [12, 7, 5]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.index("col1")
ds.show()`,Es=`ds = await load_dataset("timeserie")
ds.dateindex("date")
ds.show()`,xs=`ds = await load_dataset("bitcoin")
print("Unique values in the sources column:", ds.unique_("Source"))
dss = ds.split_("Source")
print("splitted DataSpace objects:", dss.keys())
dss["FTX"].show()`,vs=`data = {"col1": ["A", "B", "C", "D"]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.indexcol("id")
ds.show()`,Ss=`data = {"col1": [14, 8, 12], "col2": [0, 1, 0]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.drop("col2")
ds.show()`,Ms=`df = pd.DataFrame(np.linspace(1, 100, 5), columns=["num"])
ds = dataspace.from_df(df)
print("Adding a column with default value")
ds.add("num2", 1)
ds.show()`,Rs=`data = {"col1": [0, 1, 0]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.rename("col1", "new name")
ds.show()`,As=`data = {"col1": [0, 1, 0], "col2": [0, 0, 1], "col3": [1, 1, 1], "col4": [0, 0, 1]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.keep("col1", "col4")
ds.show()`,Ts=`data = {"col1": [14, 8, 12], "col2": [0, 1, 0]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.copycol("col2", "new col name")
ds.show()`,Cs=`data = {"col1": [14, 25, 3, 8, 12]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.sort("col1")
ds.show()`,Ds=`data = {"col1": [1, 0, 1, 4, 5, 1]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.exclude("col1", 1)
ds.show()`,Ns=`data = {"col1": [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.dropr([0, 4])
ds.show()`,Os=`data = {"col1": [1, 2], "col2": ["foo", "bar"]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.append(0, "baz")
ds.show()`,ks=`data = {"col1": [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.reverse()
ds.show()`,Ls=`data = {"col1": [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)

def f(row):
    # add a new column with a value
    row["newcol"] = row["col1"] + 1
    return row

ds.apply(f)
ds.show()`,Bs=`ds = await load_dataset("bitcoin")
ds.keep("mktTS", "qty")
ds.dateindex("mktTS")
ds.rsum("1S", "Datapoints per second")
ds.rename("qty", "Market volume")
ds.show()`,Is=`ds = await load_dataset("bitcoin")
ds.rmean("1S", "Datapoints per second", dateindex="mktTS")
ds.rename("px", "Mean price")
ds.show()`,Fs=`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.line_()`,Hs=`data = {"col1": ["A", "B", "C", "D", "E"], "col2": [1, 6, 2, 4, 1]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.bar_("col1:N", "col2:Q")`,Ps=`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.line_()`,js=`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.point_()`,$s=`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.area_()`,Us=`data = {"col1": ["A", "B", "C", "D", "E"], "col2": [1, 6, 2, 4, 1]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
chart = ds.bar_("col1:N", "col2:Q")
hline = ds.hline_(style={"color": "green"})
chart + hline`,qs=`data = {"col1": [1, 2, 3, 4, 4, 6, 8, 10, 12]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.diffm("col1")
ds.indexcol("id")
ds.axis("id", "col1")
c = ds.bar_()
ds.axis("id", "Diff")
d = ds.line_().encode(color=alt.value("red"))
c + d`;var Ks={load_dataset:Vn,show:Jn,cols_:Zn,count_null_:es,count_empty_:ts,count_zero_:ns,count_unique_:ss,wunique_:as,limit:is,unique_:rs,drop_nan:os,fill_nan:ls,fill_nulls:cs,fdate:ds,to_date:us,timestamps:fs,to_int:ps,to_float:hs,to_type:gs,strip:_s,strip_cols:ms,roundvals:bs,replace:ws,index:ys,dateindex:Es,split_:xs,indexcol:vs,drop:Ss,add:Ms,rename:Rs,keep:As,copycol:Ts,sort:Cs,exclude:Ds,dropr:Ns,append:Os,reverse:ks,apply:Ls,rsum:Bs,rmean:Is,axis:Fs,bar_:Hs,line_:Ps,point_:js,area_:$s,hline_:Us,diffm:qs};const Gs={class:"text-xl"},zs={class:"mt-5"},Qs={key:0},Ws=M("div",{class:"p-5 pl-8 text-lg italic"},"Example",-1),Xs={key:0,class:"w-full p-3"},Zs=ke({__name:"MethodView",setup(e){const t=ct({name:"",docstring:{}}),n=K(""),d=K({}),w=K(!1),m=K(!1);function r(){var R,D,T;m.value=!1;const o=(R=xe.currentRoute.value.params)==null?void 0:R.name;t.name="",w.value=!1,d.value={};let h;if(o)h=o.toString();else return;const _=(D=xe.currentRoute.value.meta)==null?void 0:D.source;let S;_=="chart"?S=Kn[h]:_=="toplevel"?S=Yn[h]:S=ot[h],t.name=h,t.docstring=S,t.docstring.example?n.value=t.docstring.example:n.value=(T=Ks[h])!=null?T:"",m.value=!0}const a=Le(()=>r());return dt(()=>a()),(o,h)=>(O(),k(Be,null,[M("div",Gs," Method "+ut(t.name),1),M("div",zs,[Se(Mn,{method:t},null,8,["method"])]),n.value.length>0?(O(),k("div",Qs,[Ws,m.value?(O(),k("div",Xs,[Se(ft,{id:t.name,code:n.value},null,8,["id","code"])])):G("",!0)])):G("",!0)],64))}});export{Zs as default};
