import e from"./DsCodeBlock.5a0260a8.js";import{d as r,o as l,c,a as t,b as s,F as p,e as o}from"./vendor.f90edea8.js";import"./index.184dd788.js";const _=t("div",{class:"text-xl"}," Scatter plot with tooltip ",-1),d=t("p",{class:"mt-3"},[o("This example is from the "),t("a",{href:"https://altair-viz.github.io/gallery/scatter_tooltips.html"},"Simple scatter plot with tooltips"),o(" example from Altair's examples. First load the dataset")],-1),n={class:"w-full p-3"},m=t("p",{class:"mt-5"},"Draw the chart:",-1),v=r({__name:"SimpleScatter",setup(h){const a=`ds = await load_dataset('cars')
ds.show()`,i=`ds.point_('Horsepower','Miles_per_Gallon').pw(60).encode(
    color='Origin'
).tooltip(
    ['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
).interactive()`;return(f,w)=>(l(),c(p,null,[_,d,t("div",n,[s(e,{id:"simple_scatter1",code:a}),m,s(e,{id:"simple_scatter2",class:"mt-3",code:i})])],64))}});export{v as default};
