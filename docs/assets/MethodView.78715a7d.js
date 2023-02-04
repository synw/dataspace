import{r as x,d as R}from"./index.d0cd7b5e.js";import{H as C,_ as L}from"./DsCodeBlock.413edd98.js";import{e as T,d as g,D as F,o as l,c as r,a as e,g as h,F as E,j as k,h as D,r as B,E as N,t as M,f as S}from"./vendor.3fc8d3f7.js";function q(t){const a=t.regex,s=/[\p{XID_Start}_]\p{XID_Continue}*/u,u=["and","as","assert","async","await","break","case","class","continue","def","del","elif","else","except","finally","for","from","global","if","import","in","is","lambda","match","nonlocal|10","not","or","pass","raise","return","try","while","with","yield"],i={$pattern:/[A-Za-z]\w+|__\w+__/,keyword:u,built_in:["__import__","abs","all","any","ascii","bin","bool","breakpoint","bytearray","bytes","callable","chr","classmethod","compile","complex","delattr","dict","dir","divmod","enumerate","eval","exec","filter","float","format","frozenset","getattr","globals","hasattr","hash","help","hex","id","input","int","isinstance","issubclass","iter","len","list","locals","map","max","memoryview","min","next","object","oct","open","ord","pow","print","property","range","repr","reversed","round","set","setattr","slice","sorted","staticmethod","str","sum","super","tuple","type","vars","zip"],literal:["__debug__","Ellipsis","False","None","NotImplemented","True"],type:["Any","Callable","Coroutine","Dict","List","Literal","Generic","Optional","Sequence","Set","Tuple","Type","Union"]},n={className:"meta",begin:/^(>>>|\.\.\.) /},c={className:"subst",begin:/\{/,end:/\}/,keywords:i,illegal:/#/},d={begin:/\{\{/,relevance:0},p={className:"string",contains:[t.BACKSLASH_ESCAPE],variants:[{begin:/([uU]|[bB]|[rR]|[bB][rR]|[rR][bB])?'''/,end:/'''/,contains:[t.BACKSLASH_ESCAPE,n],relevance:10},{begin:/([uU]|[bB]|[rR]|[bB][rR]|[rR][bB])?"""/,end:/"""/,contains:[t.BACKSLASH_ESCAPE,n],relevance:10},{begin:/([fF][rR]|[rR][fF]|[fF])'''/,end:/'''/,contains:[t.BACKSLASH_ESCAPE,n,d,c]},{begin:/([fF][rR]|[rR][fF]|[fF])"""/,end:/"""/,contains:[t.BACKSLASH_ESCAPE,n,d,c]},{begin:/([uU]|[rR])'/,end:/'/,relevance:10},{begin:/([uU]|[rR])"/,end:/"/,relevance:10},{begin:/([bB]|[bB][rR]|[rR][bB])'/,end:/'/},{begin:/([bB]|[bB][rR]|[rR][bB])"/,end:/"/},{begin:/([fF][rR]|[rR][fF]|[fF])'/,end:/'/,contains:[t.BACKSLASH_ESCAPE,d,c]},{begin:/([fF][rR]|[rR][fF]|[fF])"/,end:/"/,contains:[t.BACKSLASH_ESCAPE,d,c]},t.APOS_STRING_MODE,t.QUOTE_STRING_MODE]},o="[0-9](_?[0-9])*",_=`(\\b(${o}))?\\.(${o})|\\b(${o})\\.`,m=`\\b|${u.join("|")}`,w={className:"number",relevance:0,variants:[{begin:`(\\b(${o})|(${_}))[eE][+-]?(${o})[jJ]?(?=${m})`},{begin:`(${_})[jJ]?`},{begin:`\\b([1-9](_?[0-9])*|0+(_?0)*)[lLjJ]?(?=${m})`},{begin:`\\b0[bB](_?[01])+[lL]?(?=${m})`},{begin:`\\b0[oO](_?[0-7])+[lL]?(?=${m})`},{begin:`\\b0[xX](_?[0-9a-fA-F])+[lL]?(?=${m})`},{begin:`\\b(${o})[jJ](?=${m})`}]},A={className:"comment",begin:a.lookahead(/# type:/),end:/$/,keywords:i,contains:[{begin:/# type:/},{begin:/#/,end:/\b\B/,endsWithParent:!0}]},b={className:"params",variants:[{className:"",begin:/\(\s*\)/,skip:!0},{begin:/\(/,end:/\)/,excludeBegin:!0,excludeEnd:!0,keywords:i,contains:["self",n,w,p,t.HASH_COMMENT_MODE]}]};return c.contains=[p,w,n],{name:"Python",aliases:["py","gyp","ipython"],unicodeRegex:!0,keywords:i,illegal:/(<\/|->|\?)|=>/,contains:[n,w,{begin:/\bself\b/},{beginKeywords:"if",relevance:0},p,A,t.HASH_COMMENT_MODE,{match:[/\bdef/,/\s+/,s],scope:{1:"keyword",3:"title.function"},contains:[b]},{variants:[{match:[/\bclass/,/\s+/,s,/\s*/,/\(\s*/,s,/\s*\)/]},{match:[/\bclass/,/\s+/,s]}],scope:{1:"keyword",3:"title.class",6:"title.class.inherited"}},{className:"meta",begin:/^[\t ]*@/,end:/(?=#)|$/,contains:[w,b,p]}]}}const H={class:"p-3"},$={class:"px-5 py-2 code-block dark:bg-neutral-700 bg-amber-50 w-max"},O=["innerHTML"],P={class:"pl-5 mt-5"},Q=["innerHTML"],I=["innerHTML"],U={key:1,class:"mt-5"},j=e("div",{class:"text-lg italic"},"Parameters",-1),K={class:"pl-5 mt-3 space-y-2"},z=["innerHTML"],V=["innerHTML"],J=["innerHTML"],G={key:2,class:"mt-5"},X=e("div",{class:"text-lg italic"},"Return",-1),Y={class:"mt-3"},W=["innerHTML"],Z=T({__name:"MethodDoc",props:{method:{type:Object,required:!0}},setup(t){const a=t;C.registerLanguage("python",q);const s=g("");function u(){s.value=C.highlight(a.method.docstring.funcdef,{language:"python"}).value}return F(()=>u()),(y,v)=>(l(),r("div",H,[e("pre",$,[e("code",{innerHTML:s.value,style:{"white-space":"pre"}},null,8,O)]),e("div",P,[e("div",{innerHTML:t.method.docstring.description},null,8,Q),t.method.docstring.long_description?(l(),r("div",{key:0,class:"mt-3",innerHTML:t.method.docstring.long_description},null,8,I)):h("",!0),Object.keys(t.method.docstring.params).length>0?(l(),r("div",U,[j,e("ul",K,[(l(!0),r(E,null,k(Object.keys(t.method.docstring.params),f=>(l(),r("li",null,[e("span",{class:"font-bold",innerHTML:f},null,8,z),D(": "),e("span",{class:"hljs-built_in",innerHTML:t.method.docstring.params[f].type},null,8,V),D(": "),e("span",{innerHTML:t.method.docstring.params[f].description},null,8,J)]))),256))])])):h("",!0),t.method.docstring.return.type!=null?(l(),r("div",G,[X,e("div",Y,[e("span",{class:"hljs-built_in",innerHTML:t.method.docstring.return.type},null,8,W)])])):h("",!0)])]))}}),tt={funcdef:'def w(self, v: int) -> "Chart"',description:`Set the width of the chart
`,long_description:"",example:`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.line_().w(500)`,params:{v:{description:`value in pixels
`,type:`int
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},nt={funcdef:'def h(self, v: int) -> "Chart"',description:`Set the height of the chart
`,long_description:"",example:`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.line_().h(200)`,params:{v:{description:`value in pixels
`,type:`int
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},et={funcdef:'def wh(self, w: int, h: int) -> "Chart"',description:`Set the width and height of a chart
`,long_description:"",example:`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.line_().wh(500, 200)`,params:{w:{description:`width value in pixels
`,type:`int
`,default:null},h:{description:`height value in pixels
`,type:`int
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},at={funcdef:'def mw(self, v: int) -> "Chart"',description:`Configure the default mark width
`,long_description:"",example:`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.bar_().mw(7)`,params:{v:{description:`width value in pixels
`,type:`int
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},st={funcdef:'def pw(self, v: int) -> "Chart"',description:`Configure the default point width
`,long_description:"",example:`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.point_().pw(25)`,params:{v:{description:`width value in pixels
`,type:`int
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},dt={funcdef:'def color(self, v: str) -> "Chart"',description:`Configure the chart color
`,long_description:"",example:`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.area_().color("forestgreen")`,params:{v:{description:`the color value
`,type:`str
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},ot={funcdef:'def opacity(self, v: Union[int, float]) -> "Chart"',description:`Configure the chart opacity
`,long_description:"",example:`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.point_().opacity(0.5)`,params:{v:{description:`the opacity value
`,type:`Union[int, float]
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},lt={funcdef:'def tooltip(self, v: Union[str, List[str]]) -> "Chart"',description:`Configure a tooltip on hover for some colums
`,long_description:`The tooltip shows up when the user cursor goes
over the datapoint on the chart
`,example:`ds = await load_dataset("sp500")
ds.point_("date:T", "price:Q").tooltip(["date","price"])`,params:{v:{description:`column or list of columns to use for the tooltip
`,type:`Union[str, List[str]]
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},rt={funcdef:'def to(self, v: str) -> "Chart"',description:`Change the chart type for an existing chart (only for the Altair engine)
`,long_description:null,example:null,params:{v:{description:`the new chart type
`,type:`str
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},it={funcdef:'def rx(self, v=-45) -> "Chart"',description:`Rotate the chart x labels
`,long_description:null,example:null,params:{v:{description:`angle of rotation to use, defaults to -45
`,type:`int, optional
`,default:`-45
`}},raises:{},return:{name:null,type:`Chart
`}},ct={funcdef:'def nox(self) -> "Chart"',description:`Remove the x axis labels
`,long_description:"",example:`ds = await load_dataset("timeserie")
ds.axis("date:T", "data:Q")
(ds.line_().nox() + ds.point_().nox())`,params:{},raises:{},return:{name:null,type:`Chart
`}},pt={funcdef:'def noy(self) -> "Chart"',description:`Remove the y axis labels
`,long_description:"",example:`ds = await load_dataset("timeserie")
ds.axis("date:T", "data:Q")
(ds.line_().noy() + ds.point_().noy())`,params:{},raises:{},return:{name:null,type:`Chart
`}},ut={funcdef:'def title(self, v: str) -> "Chart"',description:`Add a text title to the chart
`,long_description:"",example:`ds = await load_dataset("timeserie")
ds.area_("date:T", "data:Q").title("The chart title")`,params:{v:{description:`the title text
`,type:`str
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},ft={funcdef:'def colormap(self, column: str, **kwargs) -> "Chart"',description:`Add a values based colormap to the chart
`,long_description:null,example:null,params:{column:{description:`the column to use
`,type:`str
`,default:null},kwargs:{description:`the colors and values map to use
`,type:`Dict[str,str]
`,default:null}},raises:{ArgumentError:"raised if less than two colors are provided"},return:{name:null,type:`Chart
`}},mt={funcdef:'def qcolormap(self, column: str, **kwargs) -> "Chart"',description:`Add a quantiles based colormap to the chart
`,long_description:null,example:null,params:{column:{description:`the column to use
`,type:`str
`,default:null},kwargs:{description:`the colors and values map to use
`,type:`Dict[str,str]
`,default:null}},raises:{ArgumentError:"raised if less than two colors are provided"},return:{name:null,type:`Chart
`}};var _t={w:tt,h:nt,wh:et,mw:at,pw:st,color:dt,opacity:ot,tooltip:lt,to:rt,rx:it,nox:ct,noy:pt,title:ut,colormap:ft,qcolormap:mt};const ht={funcdef:"def _load_csv(url, **kwargs) -> pd.DataFrame",description:null,long_description:null,example:null,params:{},raises:{},return:{name:null,type:null}},wt={funcdef:"def _load_django(query) -> pd.DataFrame",description:null,long_description:null,example:null,params:{},raises:{},return:{name:null,type:null}},gt={funcdef:"def from_df(df: pd.DataFrame) -> DataSpace",description:`Intialize a DataSpace from a pandas DataFrame
`,long_description:null,example:null,params:{df:{description:`a pandas <tt class="docutils literal">DataFrame</tt>
`,type:null,default:null}},raises:{},return:{name:null,type:`<tt class="docutils literal">DataSpace</tt>
`}},yt={funcdef:"def from_csv(url, **kwargs) -> DataSpace",description:`Loads csv data in the main dataframe
`,long_description:null,example:null,params:{url:{description:`url of the csv file to load:
can be absolute if it starts with <tt class="docutils literal">/</tt>
or relative if it starts with <tt class="docutils literal">./</tt>
`,type:`<tt class="docutils literal">str</tt>
`,default:null},kwargs:{description:`keyword arguments to pass to Pandas
<tt class="docutils literal">read_csv</tt> function
`,type:null,default:null}},raises:{},return:{name:null,type:`<tt class="docutils literal">DataSpace</tt>
`}},vt={funcdef:"def from_django(query) -> DataSpace",description:`Load the main dataframe from a django orm query
`,long_description:null,example:null,params:{query:{description:`django query from a model
`,type:`django query
`,default:null}},raises:{},return:{name:null,type:`<tt class="docutils literal">DataSpace</tt>
`}};var bt={_load_csv:ht,_load_django:wt,from_df:gt,from_csv:yt,from_django:vt};const xt="return dataspace.from_df([1])",Ct=`ds = await load_dataset("bitcoin")
ds.show()`,Dt=`ds = await load_dataset("bitcoin")
print(ds.cols_())
ds.show()`,St=`data = {"col1": [1, np.nan, 2, None, 3, 3]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
n = ds.count_null_("col1")
print("The column has", n, "nulls")
ds.show()`,Tt=`data = {"col1": ["foo", "", "bar", ""]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
n = ds.count_empty_("col1")
print("The column has", n, "empty values")
ds.show()`,Ft=`data = {"col1": [0, 1, 2, 0, 3, 3]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
n = ds.count_zero_("col1")
print("The column has", n, "zero values")
ds.show()`,Et=`data = {"col1": [1, 2, 2, 3, 3, 3]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
n = ds.count_unique_("col1")
print("The column has", n, "unique values")
ds.show()`,At=`data = {"col1": ["one", "two", "two", "three", "three", "three"]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
df = ds.wunique_("col1")
print("Dataframe of unique values weights:")
print(df)`,Rt=`df = pd.DataFrame(np.linspace(1, 100, 1000))
ds = dataspace.from_df(df)
print("Initial length:", len(ds.df.index))
ds.limit(10)
print("New length after limiting:", len(ds.df.index))
ds.show()`,Lt=`data = {"col1": ["A", "B", "C", "A", "B"]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
uv = ds.unique_("col1")
print("Colum unique values:", uv)
ds.show()`,kt=`data = {"col1": [14, 8, np.nan], "col2": [2, np.nan, np.nan]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
print("The col1 has", ds.count_null_("col1"), "nulls")
ds.drop_nan("col1")
ds.show()`,Bt=`data = {"col1": [14, 8, np.nan], "col2": [2, np.nan, np.nan]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.count_null_("col1")
ds.fill_nan("val", "col1")
ds.show()`,Nt=`data = {"col1": np.array([1, None, ""]), "col2": np.array([None, 0, None])}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.count_empty_("col1")
ds.count_null_("col1")
ds.fill_nulls()
ds.show()`,Mt=`ds = await load_dataset("timeserie")
print(ds.df.head())
ds.fdate("date", precision="D")
ds.show()`,qt=`ds = await load_dataset("bitcoin")
print("1. Initial dataframe:")
print(ds.df.head(1))
print("2. Colums:")
print(ds.cols_())
ds.to_date("ReceiptTS")
print("3. New column types:", ds.cols_())
ds.show()`,Ht=`ds = await load_dataset("timeserie")
print(ds.df.head())
ds.timestamps("date")
ds.show()`,$t=`data = {"col1": ["5", "8", "3"], "col2": ["8", "7", "2"]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
print("Column types:", ds.cols_())
ds.to_int("col1", "col2")
print("Column types after convert:", ds.cols_())
ds.show()`,Ot=`data = {"col1": ["0.25", "0.85", "0.58"]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
print("Column types:", ds.cols_())
ds.to_float("col1")
print("Column types after convert:", ds.cols_())
ds.show()`,Pt=`data = {"col1": [1, 0, 0]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
print("Column types:", ds.cols_())
ds.to_type(bool, "col1")
print("Column types after convert:", ds.cols_())
ds.show()`,Qt=`data = {"col1": [" one ", "two "]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
print(list(ds.df.col1))
ds.strip("col1")
print(list(ds.df.col1))
ds.show()`,It=`data = {"col1 ": [1, 2], " col2 ": [3, 4]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
print(list(ds.df.columns.values))
ds.strip_cols()
print(list(ds.df.columns.values))
ds.show()`,Ut=`data = {"col1": [1.25889, 1.25874, 1.42587]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.roundvals("col1")
ds.show()`,jt=`data = {"col1": ["a", "b", "novalue"]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.replace("col1", "novalue", "c")
ds.show()`,Kt=`data = {"col1": ["a", "b", "c"], "col2": [12, 7, 5]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.index("col1")
ds.show()`,zt=`ds = await load_dataset("timeserie")
ds.dateindex("date")
ds.show()`,Vt=`ds = await load_dataset("bitcoin")
print("Unique values in the sources column:", ds.unique_("Source"))
dss = ds.split_("Source")
print("splitted DataSpace objects:", dss.keys())
dss["FTX"].show()`,Jt=`data = {"col1": ["A", "B", "C", "D"]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.indexcol("id")
ds.show()`,Gt=`data = {"col1": [14, 8, 12], "col2": [0, 1, 0]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.drop("col2")
ds.show()`,Xt=`df = pd.DataFrame(np.linspace(1, 100, 5), columns=["num"])
ds = dataspace.from_df(df)
print("Adding a column with default value")
ds.add("num2", 1)
ds.show()`,Yt=`data = {"col1": [0, 1, 0]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.rename("col1", "new name")
ds.show()`,Wt=`data = {"col1": [0, 1, 0], "col2": [0, 0, 1], "col3": [1, 1, 1], "col4": [0, 0, 1]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.keep("col1", "col4")
ds.show()`,Zt=`data = {"col1": [14, 8, 12], "col2": [0, 1, 0]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.copycol("col2", "new col name")
ds.show()`,tn=`data = {"col1": [14, 25, 3, 8, 12]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.sort("col1")
ds.show()`,nn=`data = {"col1": [1, 0, 1, 4, 5, 1]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.exclude("col1", 1)
ds.show()`,en=`data = {"col1": [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.dropr([0, 4])
ds.show()`,an=`data = {"col1": [1, 2], "col2": ["foo", "bar"]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.append(0, "baz")
ds.show()`,sn=`data = {"col1": [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.reverse()
ds.show()`,dn=`data = {"col1": [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)

def f(row):
    # add a new column with a value
    row["newcol"] = row["col1"] + 1
    return row

ds.apply(f)
ds.show()`,on=`ds = await load_dataset("bitcoin")
ds.keep("mktTS", "qty")
ds.dateindex("mktTS")
ds.rsum("1S", "Datapoints per second")
ds.rename("qty", "Market volume")
ds.show()`,ln=`ds = await load_dataset("bitcoin")
ds.rmean("1S", "Datapoints per second", dateindex="mktTS")
ds.rename("px", "Mean price")
ds.show()`,rn=`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.line_()`,cn=`data = {"col1": ["A", "B", "C", "D", "E"], "col2": [1, 6, 2, 4, 1]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.bar_("col1:N", "col2:Q")`,pn=`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.line_()`,un=`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.point_()`,fn=`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.area_()`,mn=`data = {"col1": ["A", "B", "C", "D", "E"], "col2": [1, 6, 2, 4, 1]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
chart = ds.bar_("col1:N", "col2:Q")
hline = ds.hline_(style={"color": "green"})
chart + hline`;var _n={load_dataset:xt,show:Ct,cols_:Dt,count_null_:St,count_empty_:Tt,count_zero_:Ft,count_unique_:Et,wunique_:At,limit:Rt,unique_:Lt,drop_nan:kt,fill_nan:Bt,fill_nulls:Nt,fdate:Mt,to_date:qt,timestamps:Ht,to_int:$t,to_float:Ot,to_type:Pt,strip:Qt,strip_cols:It,roundvals:Ut,replace:jt,index:Kt,dateindex:zt,split_:Vt,indexcol:Jt,drop:Gt,add:Xt,rename:Yt,keep:Wt,copycol:Zt,sort:tn,exclude:nn,dropr:en,append:an,reverse:sn,apply:dn,rsum:on,rmean:ln,axis:rn,bar_:cn,line_:pn,point_:un,area_:fn,hline_:mn};const hn={class:"text-xl"},wn={class:"mt-5"},gn={key:0},yn=e("div",{class:"p-5 pl-8 text-lg italic"},"Example",-1),vn={key:0,class:"w-full p-3"},Dn=T({__name:"MethodView",setup(t){const a=B({name:"",docstring:{}}),s=g(""),u=g({}),y=g(!1);function v(){var p,o,_;console.log("LOAD");const i=(p=x.currentRoute.value.params)==null?void 0:p.name;a.name="",y.value=!1,u.value={};let n;if(i)n=i.toString();else return;const c=(o=x.currentRoute.value.meta)==null?void 0:o.source;let d;c=="chart"?d=_t[n]:c=="toplevel"?d=bt[n]:d=R[n],a.name=n,a.docstring=d,a.docstring.example?s.value=a.docstring.example:s.value=(_=_n[n])!=null?_:""}const f=F(()=>v());return N(()=>f()),(i,n)=>(l(),r(E,null,[e("div",hn," Method "+M(a.name),1),e("div",wn,[S(Z,{method:a},null,8,["method"])]),s.value.length>0?(l(),r("div",gn,[yn,a.name.length>0?(l(),r("div",vn,[S(L,{id:a.name,code:s.value},null,8,["id","code"])])):h("",!0)])):h("",!0)],64))}});export{Dn as default};
