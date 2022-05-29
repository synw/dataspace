import{_ as e}from"./DsCodeBlock.6593b464.js";import{e as r,o as l,c,a as t,f as s,F as p,i as o}from"./vendor.72e4ae7f.js";import"./index.f13b8fd3.js";const _=t("div",{class:"text-xl"}," Scatter plot with tooltip ",-1),d=t("p",{class:"mt-3"},[o("This example is from the "),t("a",{href:"https://altair-viz.github.io/gallery/scatter_tooltips.html"},"Simple scatter plot with tooltips"),o(" example from Altair's examples. First load the dataset")],-1),n={class:"w-full p-3"},m=t("p",{class:"mt-5"},"Draw the chart:",-1),v=r({setup(h){const a=`ds = await load_dataset('cars')
ds.show()`,i=`ds.point_('Horsepower','Miles_per_Gallon').pw(60).encode(
    color='Origin'
).tooltip(
    ['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
).interactive()`;return(f,w)=>(l(),c(p,null,[_,d,t("div",n,[s(e,{id:"simple_scatter1",code:a}),m,s(e,{id:"simple_scatter2",class:"mt-3",code:i})])],64))}});export{v as default};
