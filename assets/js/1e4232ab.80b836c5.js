"use strict";(self.webpackChunkxleap_docs=self.webpackChunkxleap_docs||[]).push([[953],{23:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>l,contentTitle:()=>i,default:()=>p,frontMatter:()=>o,metadata:()=>r,toc:()=>c});var s=n(4848),a=n(8453);const o={sidebar_position:2},i="xleap's python sdk",r={id:"tutorial-basics/create-a-document",title:"xleap's python sdk",description:"1. go to account settings and create an API Key for CLI&nbsp; open",source:"@site/docs/tutorial-basics/create-a-document.md",sourceDirName:"tutorial-basics",slug:"/tutorial-basics/create-a-document",permalink:"/docs/tutorial-basics/create-a-document",draft:!1,unlisted:!1,editUrl:"https://github.com/xleap-ai/xleap/tree/master/docs/docs/tutorial-basics/create-a-document.md",tags:[],version:"current",sidebarPosition:2,frontMatter:{sidebar_position:2},sidebar:"tutorialSidebar",previous:{title:"Typescript/Javascript",permalink:"/docs/tutorial-basics/using-js-api"},next:{title:"python requests",permalink:"/docs/tutorial-basics/create-a-blog-post"}},l={},c=[{value:"install python sdk",id:"install-python-sdk",level:2},{value:"start using sdk",id:"start-using-sdk",level:2}];function d(e){const t={a:"a",code:"code",h1:"h1",h2:"h2",li:"li",ol:"ol",pre:"pre",...(0,a.R)(),...e.components};return(0,s.jsxs)(s.Fragment,{children:[(0,s.jsx)(t.h1,{id:"xleaps-python-sdk",children:"xleap's python sdk"}),"\n",(0,s.jsxs)(t.ol,{children:["\n",(0,s.jsxs)(t.li,{children:["go to account settings and create an API Key for CLI\xa0 ",(0,s.jsx)(t.a,{href:"http://google.com",children:"open"})]}),"\n",(0,s.jsx)(t.li,{children:"copy the api key somewhere safe, it will be required in subsequent step"}),"\n",(0,s.jsx)(t.li,{children:"start sending data using one of the following methods"}),"\n"]}),"\n",(0,s.jsx)(t.h2,{id:"install-python-sdk",children:"install python sdk"}),"\n",(0,s.jsx)(t.pre,{children:(0,s.jsx)(t.code,{className:"language-shell",children:"pip install xleap\n"})}),"\n",(0,s.jsx)(t.h2,{id:"start-using-sdk",children:"start using sdk"}),"\n",(0,s.jsx)(t.pre,{children:(0,s.jsx)(t.code,{className:"language-python",metastring:'title="setup.py"',children:'from xleap.client import DataPointCreate, XleapApi\n\nAPI_KEY = "<********* private key from dashboard>"  # should be private\n\nclient = XleapApi(api_key=API_KEY)\n\nresponse = client.create_data_point_create(\n    DataPointCreate(\n        **{\n            "question": "<Your question or prompt template with {context_var}>",\n            "answer": "<llm response as text or stringified json>",\n            "contexts": [\n                "<array of strings sent to the llm model as key value pair>",\n                "context_var: this is sample context",\n            ],\n            "ground_truths": [],\n        }\n    )\n)\n\n\nprint(response)\n'})})]})}function p(e={}){const{wrapper:t}={...(0,a.R)(),...e.components};return t?(0,s.jsx)(t,{...e,children:(0,s.jsx)(d,{...e})}):d(e)}},8453:(e,t,n)=>{n.d(t,{R:()=>i,x:()=>r});var s=n(6540);const a={},o=s.createContext(a);function i(e){const t=s.useContext(o);return s.useMemo((function(){return"function"==typeof e?e(t):{...t,...e}}),[t,e])}function r(e){let t;return t=e.disableParentContext?"function"==typeof e.components?e.components(a):e.components||a:i(e.components),s.createElement(o.Provider,{value:t},e.children)}}}]);