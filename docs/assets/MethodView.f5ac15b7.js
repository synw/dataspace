import{r as x,d as R}from"./index.f13b8fd3.js";import{H as C,_ as L}from"./DsCodeBlock.6593b464.js";import{e as S,d as h,D as T,o as p,c as u,a as n,g,F,j as k,i as E,E as B,t as N,f as D}from"./vendor.72e4ae7f.js";function M(t){const l=t.regex,a=/[\p{XID_Start}_]\p{XID_Continue}*/u,f=["and","as","assert","async","await","break","class","continue","def","del","elif","else","except","finally","for","from","global","if","import","in","is","lambda","nonlocal|10","not","or","pass","raise","return","try","while","with","yield"],r={$pattern:/[A-Za-z]\w+|__\w+__/,keyword:f,built_in:["__import__","abs","all","any","ascii","bin","bool","breakpoint","bytearray","bytes","callable","chr","classmethod","compile","complex","delattr","dict","dir","divmod","enumerate","eval","exec","filter","float","format","frozenset","getattr","globals","hasattr","hash","help","hex","id","input","int","isinstance","issubclass","iter","len","list","locals","map","max","memoryview","min","next","object","oct","open","ord","pow","print","property","range","repr","reversed","round","set","setattr","slice","sorted","staticmethod","str","sum","super","tuple","type","vars","zip"],literal:["__debug__","Ellipsis","False","None","NotImplemented","True"],type:["Any","Callable","Coroutine","Dict","List","Literal","Generic","Optional","Sequence","Set","Tuple","Type","Union"]},e={className:"meta",begin:/^(>>>|\.\.\.) /},i={className:"subst",begin:/\{/,end:/\}/,keywords:r,illegal:/#/},s={begin:/\{\{/,relevance:0},c={className:"string",contains:[t.BACKSLASH_ESCAPE],variants:[{begin:/([uU]|[bB]|[rR]|[bB][rR]|[rR][bB])?'''/,end:/'''/,contains:[t.BACKSLASH_ESCAPE,e],relevance:10},{begin:/([uU]|[bB]|[rR]|[bB][rR]|[rR][bB])?"""/,end:/"""/,contains:[t.BACKSLASH_ESCAPE,e],relevance:10},{begin:/([fF][rR]|[rR][fF]|[fF])'''/,end:/'''/,contains:[t.BACKSLASH_ESCAPE,e,s,i]},{begin:/([fF][rR]|[rR][fF]|[fF])"""/,end:/"""/,contains:[t.BACKSLASH_ESCAPE,e,s,i]},{begin:/([uU]|[rR])'/,end:/'/,relevance:10},{begin:/([uU]|[rR])"/,end:/"/,relevance:10},{begin:/([bB]|[bB][rR]|[rR][bB])'/,end:/'/},{begin:/([bB]|[bB][rR]|[rR][bB])"/,end:/"/},{begin:/([fF][rR]|[rR][fF]|[fF])'/,end:/'/,contains:[t.BACKSLASH_ESCAPE,s,i]},{begin:/([fF][rR]|[rR][fF]|[fF])"/,end:/"/,contains:[t.BACKSLASH_ESCAPE,s,i]},t.APOS_STRING_MODE,t.QUOTE_STRING_MODE]},d="[0-9](_?[0-9])*",_=`(\\b(${d}))?\\.(${d})|\\b(${d})\\.`,o=`\\b|${f.join("|")}`,w={className:"number",relevance:0,variants:[{begin:`(\\b(${d})|(${_}))[eE][+-]?(${d})[jJ]?(?=${o})`},{begin:`(${_})[jJ]?`},{begin:`\\b([1-9](_?[0-9])*|0+(_?0)*)[lLjJ]?(?=${o})`},{begin:`\\b0[bB](_?[01])+[lL]?(?=${o})`},{begin:`\\b0[oO](_?[0-7])+[lL]?(?=${o})`},{begin:`\\b0[xX](_?[0-9a-fA-F])+[lL]?(?=${o})`},{begin:`\\b(${d})[jJ](?=${o})`}]},A={className:"comment",begin:l.lookahead(/# type:/),end:/$/,keywords:r,contains:[{begin:/# type:/},{begin:/#/,end:/\b\B/,endsWithParent:!0}]},b={className:"params",variants:[{className:"",begin:/\(\s*\)/,skip:!0},{begin:/\(/,end:/\)/,excludeBegin:!0,excludeEnd:!0,keywords:r,contains:["self",e,w,c,t.HASH_COMMENT_MODE]}]};return i.contains=[c,w,e],{name:"Python",aliases:["py","gyp","ipython"],unicodeRegex:!0,keywords:r,illegal:/(<\/|->|\?)|=>/,contains:[e,w,{begin:/\bself\b/},{beginKeywords:"if",relevance:0},c,A,t.HASH_COMMENT_MODE,{match:[/\bdef/,/\s+/,a],scope:{1:"keyword",3:"title.function"},contains:[b]},{variants:[{match:[/\bclass/,/\s+/,a,/\s*/,/\(\s*/,a,/\s*\)/]},{match:[/\bclass/,/\s+/,a]}],scope:{1:"keyword",3:"title.class",6:"title.class.inherited"}},{className:"meta",begin:/^[\t ]*@/,end:/(?=#)|$/,contains:[w,b,c]}]}}const q={class:"p-3"},H={class:"px-5 py-2 code-block dark:bg-neutral-700 bg-amber-50 w-max"},$=["innerHTML"],P={class:"pl-5 mt-5"},Q=["innerHTML"],I=["innerHTML"],O={key:1,class:"mt-5"},U=n("div",{class:"text-lg italic"},"Parameters",-1),j={class:"pl-5 mt-3 space-y-2"},K=["innerHTML"],z=E(": "),J=["innerHTML"],V=E(": "),G=["innerHTML"],X={key:2,class:"mt-5"},Y=n("div",{class:"text-lg italic"},"Return",-1),W={class:"mt-3"},Z=["innerHTML"],tt=S({props:{method:{type:Object,required:!0}},setup(t){const l=t;C.registerLanguage("python",M);const a=h("");function f(){a.value=C.highlight(l.method.docstring.funcdef,{language:"python"}).value}return T(()=>f()),(y,v)=>(p(),u("div",q,[n("pre",H,[n("code",{innerHTML:a.value,style:{"white-space":"pre"}},null,8,$)]),n("div",P,[n("div",{innerHTML:t.method.docstring.description},null,8,Q),t.method.docstring.long_description?(p(),u("div",{key:0,class:"mt-3",innerHTML:t.method.docstring.long_description},null,8,I)):g("",!0),Object.keys(t.method.docstring.params).length>0?(p(),u("div",O,[U,n("ul",j,[(p(!0),u(F,null,k(Object.keys(t.method.docstring.params),m=>(p(),u("li",null,[n("span",{class:"font-bold",innerHTML:m},null,8,K),z,n("span",{class:"hljs-built_in",innerHTML:t.method.docstring.params[m].type},null,8,J),V,n("span",{innerHTML:t.method.docstring.params[m].description},null,8,G)]))),256))])])):g("",!0),t.method.docstring.return.type!=null?(p(),u("div",X,[Y,n("div",W,[n("span",{class:"hljs-built_in",innerHTML:t.method.docstring.return.type},null,8,Z)])])):g("",!0)])]))}}),nt={funcdef:'def w(self, v: int) -> "Chart"',description:`Set the width of the chart
`,long_description:"",example:`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.line_().w(500)`,params:{v:{description:`value in pixels
`,type:`int
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},et={funcdef:'def h(self, v: int) -> "Chart"',description:`Set the height of the chart
`,long_description:"",example:`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.line_().h(200)`,params:{v:{description:`value in pixels
`,type:`int
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},at={funcdef:'def wh(self, w: int, h: int) -> "Chart"',description:`Set the width and height of a chart
`,long_description:"",example:`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.line_().wh(500, 200)`,params:{w:{description:`width value in pixels
`,type:`int
`,default:null},h:{description:`height value in pixels
`,type:`int
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},st={funcdef:'def mw(self, v: int) -> "Chart"',description:`Configure the default mark width
`,long_description:"",example:`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.bar_().mw(7)`,params:{v:{description:`width value in pixels
`,type:`int
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},dt={funcdef:'def pw(self, v: int) -> "Chart"',description:`Configure the default point width
`,long_description:"",example:`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.point_().pw(25)`,params:{v:{description:`width value in pixels
`,type:`int
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},ot={funcdef:'def color(self, v: str) -> "Chart"',description:`Configure the chart color
`,long_description:"",example:`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.area_().color("forestgreen")`,params:{v:{description:`the color value
`,type:`str
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},lt={funcdef:'def opacity(self, v: Union[int, float]) -> "Chart"',description:`Configure the chart opacity
`,long_description:"",example:`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.point_().opacity(0.5)`,params:{v:{description:`the opacity value
`,type:`Union[int, float]
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},rt={funcdef:'def tooltip(self, v: Union[str, List[str]]) -> "Chart"',description:`Configure a tooltip on hover for some colums
`,long_description:`The tooltip shows up when the user cursor goes
over the datapoint on the chart
`,example:`ds = await load_dataset("sp500")
ds.point_("date:T", "price:Q").tooltip(["date","price"])`,params:{v:{description:`column or list of columns to use for the tooltip
`,type:`Union[str, List[str]]
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},it={funcdef:'def to(self, v: str) -> "Chart"',description:`Change the chart type for an existing chart (only for the Altair engine)
`,long_description:null,example:null,params:{v:{description:`the new chart type
`,type:`str
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},ct={funcdef:'def rx(self, v=-45) -> "Chart"',description:`Rotate the chart x labels
`,long_description:null,example:null,params:{v:{description:`angle of rotation to use, defaults to -45
`,type:`int, optional
`,default:`-45
`}},raises:{},return:{name:null,type:`Chart
`}},pt={funcdef:'def nox(self) -> "Chart"',description:`Remove the x axis labels
`,long_description:"",example:`ds = await load_dataset("timeserie")
ds.axis("date:T", "data:Q")
(ds.line_().nox() + ds.point_().nox())`,params:{},raises:{},return:{name:null,type:`Chart
`}},ut={funcdef:'def noy(self) -> "Chart"',description:`Remove the y axis labels
`,long_description:"",example:`ds = await load_dataset("timeserie")
ds.axis("date:T", "data:Q")
(ds.line_().noy() + ds.point_().noy())`,params:{},raises:{},return:{name:null,type:`Chart
`}},ft={funcdef:'def title(self, v: str) -> "Chart"',description:`Add a text title to the chart
`,long_description:"",example:`ds = await load_dataset("timeserie")
ds.area_("date:T", "data:Q").title("The chart title")`,params:{v:{description:`the title text
`,type:`str
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},mt={funcdef:'def colormap(self, column: str, **kwargs) -> "Chart"',description:`Add a values based colormap to the chart
`,long_description:null,example:null,params:{column:{description:`the column to use
`,type:`str
`,default:null},kwargs:{description:`the colors and values map to use
`,type:`Dict[str,str]
`,default:null}},raises:{ArgumentError:"raised if less than two colors are provided"},return:{name:null,type:`Chart
`}},_t={funcdef:'def qcolormap(self, column: str, **kwargs) -> "Chart"',description:`Add a quantiles based colormap to the chart
`,long_description:null,example:null,params:{column:{description:`the column to use
`,type:`str
`,default:null},kwargs:{description:`the colors and values map to use
`,type:`Dict[str,str]
`,default:null}},raises:{ArgumentError:"raised if less than two colors are provided"},return:{name:null,type:`Chart
`}};var ht={w:nt,h:et,wh:at,mw:st,pw:dt,color:ot,opacity:lt,tooltip:rt,to:it,rx:ct,nox:pt,noy:ut,title:ft,colormap:mt,qcolormap:_t};const wt={funcdef:"def _load_csv(url, **kwargs) -> pd.DataFrame",description:null,long_description:null,example:null,params:{},raises:{},return:{name:null,type:null}},gt={funcdef:"def _load_django(query) -> pd.DataFrame",description:null,long_description:null,example:null,params:{},raises:{},return:{name:null,type:null}},yt={funcdef:"def from_df(df: pd.DataFrame) -> DataSpace",description:`Intialize a DataSpace from a pandas DataFrame
`,long_description:null,example:null,params:{df:{description:`a pandas <tt class="docutils literal">DataFrame</tt>
`,type:null,default:null}},raises:{},return:{name:null,type:`<tt class="docutils literal">DataSpace</tt>
`}},vt={funcdef:"def from_csv(url, **kwargs) -> DataSpace",description:`Loads csv data in the main dataframe
`,long_description:null,example:null,params:{url:{description:`url of the csv file to load:
can be absolute if it starts with <tt class="docutils literal">/</tt>
or relative if it starts with <tt class="docutils literal">./</tt>
`,type:`<tt class="docutils literal">str</tt>
`,default:null},kwargs:{description:`keyword arguments to pass to Pandas
<tt class="docutils literal">read_csv</tt> function
`,type:null,default:null}},raises:{},return:{name:null,type:`<tt class="docutils literal">DataSpace</tt>
`}},bt={funcdef:"def from_django(query) -> DataSpace",description:`Load the main dataframe from a django orm query
`,long_description:null,example:null,params:{query:{description:`django query from a model
`,type:`django query
`,default:null}},raises:{},return:{name:null,type:`<tt class="docutils literal">DataSpace</tt>
`}};var xt={_load_csv:wt,_load_django:gt,from_df:yt,from_csv:vt,from_django:bt};const Ct="return dataspace.from_df([1])",Dt=`ds = await load_dataset("bitcoin")
ds.show()`,St=`ds = await load_dataset("bitcoin")
print(ds.cols_())
ds.show()`,Tt=`data = {"col1": [1, np.nan, 2, None, 3, 3]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
n = ds.count_null_("col1")
print("The column has", n, "nulls")
ds.show()`,Ft=`data = {"col1": ["foo", "", "bar", ""]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
n = ds.count_empty_("col1")
print("The column has", n, "empty values")
ds.show()`,Et=`data = {"col1": [0, 1, 2, 0, 3, 3]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
n = ds.count_zero_("col1")
print("The column has", n, "zero values")
ds.show()`,At=`data = {"col1": [1, 2, 2, 3, 3, 3]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
n = ds.count_unique_("col1")
print("The column has", n, "unique values")
ds.show()`,Rt=`data = {"col1": ["one", "two", "two", "three", "three", "three"]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
df = ds.wunique_("col1")
print("Dataframe of unique values weights:")
print(df)`,Lt=`df = pd.DataFrame(np.linspace(1, 100, 1000))
ds = dataspace.from_df(df)
print("Initial length:", len(ds.df.index))
ds.limit(10)
print("New length after limiting:", len(ds.df.index))
ds.show()`,kt=`data = {"col1": ["A", "B", "C", "A", "B"]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
uv = ds.unique_("col1")
print("Colum unique values:", uv)
ds.show()`,Bt=`data = {"col1": [14, 8, np.nan], "col2": [2, np.nan, np.nan]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
print("The col1 has", ds.count_null_("col1"), "nulls")
ds.drop_nan("col1")
ds.show()`,Nt=`data = {"col1": [14, 8, np.nan], "col2": [2, np.nan, np.nan]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.count_null_("col1")
ds.fill_nan("val", "col1")
ds.show()`,Mt=`data = {"col1": np.array([1, None, ""]), "col2": np.array([None, 0, None])}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.count_empty_("col1")
ds.count_null_("col1")
ds.fill_nulls()
ds.show()`,qt=`ds = await load_dataset("timeserie")
print(ds.df.head())
ds.fdate("date", precision="D")
ds.show()`,Ht=`ds = await load_dataset("bitcoin")
print("1. Initial dataframe:")
print(ds.df.head(1))
print("2. Colums:")
print(ds.cols_())
ds.to_date("ReceiptTS")
print("3. New column types:", ds.cols_())
ds.show()`,$t=`ds = await load_dataset("timeserie")
print(ds.df.head())
ds.timestamps("date")
ds.show()`,Pt=`data = {"col1": ["5", "8", "3"], "col2": ["8", "7", "2"]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
print("Column types:", ds.cols_())
ds.to_int("col1", "col2")
print("Column types after convert:", ds.cols_())
ds.show()`,Qt=`data = {"col1": ["0.25", "0.85", "0.58"]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
print("Column types:", ds.cols_())
ds.to_float("col1")
print("Column types after convert:", ds.cols_())
ds.show()`,It=`data = {"col1": [1, 0, 0]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
print("Column types:", ds.cols_())
ds.to_type(bool, "col1")
print("Column types after convert:", ds.cols_())
ds.show()`,Ot=`data = {"col1": [" one ", "two "]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
print(list(ds.df.col1))
ds.strip("col1")
print(list(ds.df.col1))
ds.show()`,Ut=`data = {"col1 ": [1, 2], " col2 ": [3, 4]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
print(list(ds.df.columns.values))
ds.strip_cols()
print(list(ds.df.columns.values))
ds.show()`,jt=`data = {"col1": [1.25889, 1.25874, 1.42587]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.roundvals("col1")
ds.show()`,Kt=`data = {"col1": ["a", "b", "novalue"]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.replace("col1", "novalue", "c")
ds.show()`,zt=`data = {"col1": ["a", "b", "c"], "col2": [12, 7, 5]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.index("col1")
ds.show()`,Jt=`ds = await load_dataset("timeserie")
ds.dateindex("date")
ds.show()`,Vt=`ds = await load_dataset("bitcoin")
print("Unique values in the sources column:", ds.unique_("Source"))
dss = ds.split_("Source")
print("splitted DataSpace objects:", dss.keys())
dss["FTX"].show()`,Gt=`data = {"col1": ["A", "B", "C", "D"]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.indexcol("id")
ds.show()`,Xt=`data = {"col1": [14, 8, 12], "col2": [0, 1, 0]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.drop("col2")
ds.show()`,Yt=`df = pd.DataFrame(np.linspace(1, 100, 5), columns=["num"])
ds = dataspace.from_df(df)
print("Adding a column with default value")
ds.add("num2", 1)
ds.show()`,Wt=`data = {"col1": [0, 1, 0]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.rename("col1", "new name")
ds.show()`,Zt=`data = {"col1": [0, 1, 0], "col2": [0, 0, 1], "col3": [1, 1, 1], "col4": [0, 0, 1]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.keep("col1", "col4")
ds.show()`,tn=`data = {"col1": [14, 8, 12], "col2": [0, 1, 0]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.copycol("col2", "new col name")
ds.show()`,nn=`data = {"col1": [14, 25, 3, 8, 12]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.sort("col1")
ds.show()`,en=`data = {"col1": [1, 0, 1, 4, 5, 1]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.exclude("col1", 1)
ds.show()`,an=`data = {"col1": [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.dropr([0, 4])
ds.show()`,sn=`data = {"col1": [1, 2], "col2": ["foo", "bar"]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.append(0, "baz")
ds.show()`,dn=`data = {"col1": [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.reverse()
ds.show()`,on=`data = {"col1": [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)

def f(row):
    # add a new column with a value
    row["newcol"] = row["col1"] + 1
    return row

ds.apply(f)
ds.show()`,ln=`ds = await load_dataset("bitcoin")
ds.keep("mktTS", "qty")
ds.dateindex("mktTS")
ds.rsum("1S", "Datapoints per second")
ds.rename("qty", "Market volume")
ds.show()`,rn=`ds = await load_dataset("bitcoin")
ds.rmean("1S", "Datapoints per second", dateindex="mktTS")
ds.rename("px", "Mean price")
ds.show()`,cn=`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.line_()`,pn=`data = {"col1": ["A", "B", "C", "D", "E"], "col2": [1, 6, 2, 4, 1]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.bar_("col1:N", "col2:Q")`,un=`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.line_()`,fn=`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.point_()`,mn=`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.area_()`,_n=`data = {"col1": ["A", "B", "C", "D", "E"], "col2": [1, 6, 2, 4, 1]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
chart = ds.bar_("col1:N", "col2:Q")
hline = ds.hline_(style={"color": "green"})
chart + hline`;var hn={load_dataset:Ct,show:Dt,cols_:St,count_null_:Tt,count_empty_:Ft,count_zero_:Et,count_unique_:At,wunique_:Rt,limit:Lt,unique_:kt,drop_nan:Bt,fill_nan:Nt,fill_nulls:Mt,fdate:qt,to_date:Ht,timestamps:$t,to_int:Pt,to_float:Qt,to_type:It,strip:Ot,strip_cols:Ut,roundvals:jt,replace:Kt,index:zt,dateindex:Jt,split_:Vt,indexcol:Gt,drop:Xt,add:Yt,rename:Wt,keep:Zt,copycol:tn,sort:nn,exclude:en,dropr:an,append:sn,reverse:dn,apply:on,rsum:ln,rmean:rn,axis:cn,bar_:pn,line_:un,point_:fn,area_:mn,hline_:_n};const wn={class:"text-xl"},gn={class:"mt-5"},yn={key:0},vn=n("div",{class:"p-5 pl-8 text-lg italic"},"Example",-1),bn={class:"w-full p-3"},Sn=S({setup(t){const l=h({name:"",docstring:{}}),a=h(""),f=h({}),y=h(!1);function v(){var d,_,o;const r=(d=x.currentRoute.value.params)==null?void 0:d.name;y.value=!1,f.value={};let e;if(r)e=r.toString();else return;const i=(_=x.currentRoute.value.meta)==null?void 0:_.source;let s;i=="chart"?s=ht[e]:i=="toplevel"?s=xt[e]:s=R[e];const c={name:e,docstring:s};l.value=c,c.docstring.example?a.value=c.docstring.example:a.value=(o=hn[e])!=null?o:""}const m=T(()=>v());return B(()=>m()),(r,e)=>(p(),u(F,null,[n("div",wn," Method "+N(l.value.name),1),n("div",gn,[D(tt,{method:l.value},null,8,["method"])]),a.value.length>0?(p(),u("div",yn,[vn,n("div",bn,[D(L,{id:l.value.name,code:a.value},null,8,["id","code"])])])):g("",!0)],64))}});export{Sn as default};
