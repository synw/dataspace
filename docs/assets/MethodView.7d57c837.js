import{r as C,d as L}from"./index.35991a08.js";import{H as D,_ as k}from"./DsCodeBlock.2fc314f4.js";import{e as T,d as y,D as F,o as l,c as r,a as e,g as h,F as E,j as B,i as A,r as N,E as M,t as q,u as g,f as S}from"./vendor.a456179a.js";function H(t){const a=t.regex,s=/[\p{XID_Start}_]\p{XID_Continue}*/u,u=["and","as","assert","async","await","break","class","continue","def","del","elif","else","except","finally","for","from","global","if","import","in","is","lambda","nonlocal|10","not","or","pass","raise","return","try","while","with","yield"],i={$pattern:/[A-Za-z]\w+|__\w+__/,keyword:u,built_in:["__import__","abs","all","any","ascii","bin","bool","breakpoint","bytearray","bytes","callable","chr","classmethod","compile","complex","delattr","dict","dir","divmod","enumerate","eval","exec","filter","float","format","frozenset","getattr","globals","hasattr","hash","help","hex","id","input","int","isinstance","issubclass","iter","len","list","locals","map","max","memoryview","min","next","object","oct","open","ord","pow","print","property","range","repr","reversed","round","set","setattr","slice","sorted","staticmethod","str","sum","super","tuple","type","vars","zip"],literal:["__debug__","Ellipsis","False","None","NotImplemented","True"],type:["Any","Callable","Coroutine","Dict","List","Literal","Generic","Optional","Sequence","Set","Tuple","Type","Union"]},n={className:"meta",begin:/^(>>>|\.\.\.) /},c={className:"subst",begin:/\{/,end:/\}/,keywords:i,illegal:/#/},d={begin:/\{\{/,relevance:0},p={className:"string",contains:[t.BACKSLASH_ESCAPE],variants:[{begin:/([uU]|[bB]|[rR]|[bB][rR]|[rR][bB])?'''/,end:/'''/,contains:[t.BACKSLASH_ESCAPE,n],relevance:10},{begin:/([uU]|[bB]|[rR]|[bB][rR]|[rR][bB])?"""/,end:/"""/,contains:[t.BACKSLASH_ESCAPE,n],relevance:10},{begin:/([fF][rR]|[rR][fF]|[fF])'''/,end:/'''/,contains:[t.BACKSLASH_ESCAPE,n,d,c]},{begin:/([fF][rR]|[rR][fF]|[fF])"""/,end:/"""/,contains:[t.BACKSLASH_ESCAPE,n,d,c]},{begin:/([uU]|[rR])'/,end:/'/,relevance:10},{begin:/([uU]|[rR])"/,end:/"/,relevance:10},{begin:/([bB]|[bB][rR]|[rR][bB])'/,end:/'/},{begin:/([bB]|[bB][rR]|[rR][bB])"/,end:/"/},{begin:/([fF][rR]|[rR][fF]|[fF])'/,end:/'/,contains:[t.BACKSLASH_ESCAPE,d,c]},{begin:/([fF][rR]|[rR][fF]|[fF])"/,end:/"/,contains:[t.BACKSLASH_ESCAPE,d,c]},t.APOS_STRING_MODE,t.QUOTE_STRING_MODE]},o="[0-9](_?[0-9])*",_=`(\\b(${o}))?\\.(${o})|\\b(${o})\\.`,m=`\\b|${u.join("|")}`,w={className:"number",relevance:0,variants:[{begin:`(\\b(${o})|(${_}))[eE][+-]?(${o})[jJ]?(?=${m})`},{begin:`(${_})[jJ]?`},{begin:`\\b([1-9](_?[0-9])*|0+(_?0)*)[lLjJ]?(?=${m})`},{begin:`\\b0[bB](_?[01])+[lL]?(?=${m})`},{begin:`\\b0[oO](_?[0-7])+[lL]?(?=${m})`},{begin:`\\b0[xX](_?[0-9a-fA-F])+[lL]?(?=${m})`},{begin:`\\b(${o})[jJ](?=${m})`}]},R={className:"comment",begin:a.lookahead(/# type:/),end:/$/,keywords:i,contains:[{begin:/# type:/},{begin:/#/,end:/\b\B/,endsWithParent:!0}]},x={className:"params",variants:[{className:"",begin:/\(\s*\)/,skip:!0},{begin:/\(/,end:/\)/,excludeBegin:!0,excludeEnd:!0,keywords:i,contains:["self",n,w,p,t.HASH_COMMENT_MODE]}]};return c.contains=[p,w,n],{name:"Python",aliases:["py","gyp","ipython"],unicodeRegex:!0,keywords:i,illegal:/(<\/|->|\?)|=>/,contains:[n,w,{begin:/\bself\b/},{beginKeywords:"if",relevance:0},p,R,t.HASH_COMMENT_MODE,{match:[/\bdef/,/\s+/,s],scope:{1:"keyword",3:"title.function"},contains:[x]},{variants:[{match:[/\bclass/,/\s+/,s,/\s*/,/\(\s*/,s,/\s*\)/]},{match:[/\bclass/,/\s+/,s]}],scope:{1:"keyword",3:"title.class",6:"title.class.inherited"}},{className:"meta",begin:/^[\t ]*@/,end:/(?=#)|$/,contains:[w,x,p]}]}}const $={class:"p-3"},O={class:"px-5 py-2 code-block dark:bg-neutral-700 bg-amber-50 w-max"},P=["innerHTML"],Q={class:"pl-5 mt-5"},I=["innerHTML"],U=["innerHTML"],j={key:1,class:"mt-5"},K=e("div",{class:"text-lg italic"},"Parameters",-1),z={class:"pl-5 mt-3 space-y-2"},J=["innerHTML"],V=A(": "),G=["innerHTML"],X=A(": "),Y=["innerHTML"],W={key:2,class:"mt-5"},Z=e("div",{class:"text-lg italic"},"Return",-1),tt={class:"mt-3"},nt=["innerHTML"],et=T({props:{method:{type:Object,required:!0}},setup(t){const a=t;D.registerLanguage("python",H);const s=y("");function u(){s.value=D.highlight(a.method.docstring.funcdef,{language:"python"}).value}return F(()=>u()),(v,b)=>(l(),r("div",$,[e("pre",O,[e("code",{innerHTML:s.value,style:{"white-space":"pre"}},null,8,P)]),e("div",Q,[e("div",{innerHTML:t.method.docstring.description},null,8,I),t.method.docstring.long_description?(l(),r("div",{key:0,class:"mt-3",innerHTML:t.method.docstring.long_description},null,8,U)):h("",!0),Object.keys(t.method.docstring.params).length>0?(l(),r("div",j,[K,e("ul",z,[(l(!0),r(E,null,B(Object.keys(t.method.docstring.params),f=>(l(),r("li",null,[e("span",{class:"font-bold",innerHTML:f},null,8,J),V,e("span",{class:"hljs-built_in",innerHTML:t.method.docstring.params[f].type},null,8,G),X,e("span",{innerHTML:t.method.docstring.params[f].description},null,8,Y)]))),256))])])):h("",!0),t.method.docstring.return.type!=null?(l(),r("div",W,[Z,e("div",tt,[e("span",{class:"hljs-built_in",innerHTML:t.method.docstring.return.type},null,8,nt)])])):h("",!0)])]))}}),at={funcdef:'def w(self, v: int) -> "Chart"',description:`Set the width of the chart
`,long_description:"",example:`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.line_().w(500)`,params:{v:{description:`value in pixels
`,type:`int
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},st={funcdef:'def h(self, v: int) -> "Chart"',description:`Set the height of the chart
`,long_description:"",example:`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.line_().h(200)`,params:{v:{description:`value in pixels
`,type:`int
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},dt={funcdef:'def wh(self, w: int, h: int) -> "Chart"',description:`Set the width and height of a chart
`,long_description:"",example:`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.line_().wh(500, 200)`,params:{w:{description:`width value in pixels
`,type:`int
`,default:null},h:{description:`height value in pixels
`,type:`int
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},ot={funcdef:'def mw(self, v: int) -> "Chart"',description:`Configure the default mark width
`,long_description:"",example:`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.bar_().mw(7)`,params:{v:{description:`width value in pixels
`,type:`int
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},lt={funcdef:'def pw(self, v: int) -> "Chart"',description:`Configure the default point width
`,long_description:"",example:`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.point_().pw(25)`,params:{v:{description:`width value in pixels
`,type:`int
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},rt={funcdef:'def color(self, v: str) -> "Chart"',description:`Configure the chart color
`,long_description:"",example:`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.area_().color("forestgreen")`,params:{v:{description:`the color value
`,type:`str
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},it={funcdef:'def opacity(self, v: Union[int, float]) -> "Chart"',description:`Configure the chart opacity
`,long_description:"",example:`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.point_().opacity(0.5)`,params:{v:{description:`the opacity value
`,type:`Union[int, float]
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},ct={funcdef:'def tooltip(self, v: Union[str, List[str]]) -> "Chart"',description:`Configure a tooltip on hover for some colums
`,long_description:`The tooltip shows up when the user cursor goes
over the datapoint on the chart
`,example:`ds = await load_dataset("sp500")
ds.point_("date:T", "price:Q").tooltip(["date","price"])`,params:{v:{description:`column or list of columns to use for the tooltip
`,type:`Union[str, List[str]]
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},pt={funcdef:'def to(self, v: str) -> "Chart"',description:`Change the chart type for an existing chart (only for the Altair engine)
`,long_description:null,example:null,params:{v:{description:`the new chart type
`,type:`str
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},ut={funcdef:'def rx(self, v=-45) -> "Chart"',description:`Rotate the chart x labels
`,long_description:null,example:null,params:{v:{description:`angle of rotation to use, defaults to -45
`,type:`int, optional
`,default:`-45
`}},raises:{},return:{name:null,type:`Chart
`}},ft={funcdef:'def nox(self) -> "Chart"',description:`Remove the x axis labels
`,long_description:"",example:`ds = await load_dataset("timeserie")
ds.axis("date:T", "data:Q")
(ds.line_().nox() + ds.point_().nox())`,params:{},raises:{},return:{name:null,type:`Chart
`}},mt={funcdef:'def noy(self) -> "Chart"',description:`Remove the y axis labels
`,long_description:"",example:`ds = await load_dataset("timeserie")
ds.axis("date:T", "data:Q")
(ds.line_().noy() + ds.point_().noy())`,params:{},raises:{},return:{name:null,type:`Chart
`}},_t={funcdef:'def title(self, v: str) -> "Chart"',description:`Add a text title to the chart
`,long_description:"",example:`ds = await load_dataset("timeserie")
ds.area_("date:T", "data:Q").title("The chart title")`,params:{v:{description:`the title text
`,type:`str
`,default:null}},raises:{},return:{name:null,type:`Chart
`}},ht={funcdef:'def colormap(self, column: str, **kwargs) -> "Chart"',description:`Add a values based colormap to the chart
`,long_description:null,example:null,params:{column:{description:`the column to use
`,type:`str
`,default:null},kwargs:{description:`the colors and values map to use
`,type:`Dict[str,str]
`,default:null}},raises:{ArgumentError:"raised if less than two colors are provided"},return:{name:null,type:`Chart
`}},wt={funcdef:'def qcolormap(self, column: str, **kwargs) -> "Chart"',description:`Add a quantiles based colormap to the chart
`,long_description:null,example:null,params:{column:{description:`the column to use
`,type:`str
`,default:null},kwargs:{description:`the colors and values map to use
`,type:`Dict[str,str]
`,default:null}},raises:{ArgumentError:"raised if less than two colors are provided"},return:{name:null,type:`Chart
`}};var gt={w:at,h:st,wh:dt,mw:ot,pw:lt,color:rt,opacity:it,tooltip:ct,to:pt,rx:ut,nox:ft,noy:mt,title:_t,colormap:ht,qcolormap:wt};const yt={funcdef:"def _load_csv(url, **kwargs) -> pd.DataFrame",description:null,long_description:null,example:null,params:{},raises:{},return:{name:null,type:null}},vt={funcdef:"def _load_django(query) -> pd.DataFrame",description:null,long_description:null,example:null,params:{},raises:{},return:{name:null,type:null}},bt={funcdef:"def from_df(df: pd.DataFrame) -> DataSpace",description:`Intialize a DataSpace from a pandas DataFrame
`,long_description:null,example:null,params:{df:{description:`a pandas <tt class="docutils literal">DataFrame</tt>
`,type:null,default:null}},raises:{},return:{name:null,type:`<tt class="docutils literal">DataSpace</tt>
`}},xt={funcdef:"def from_csv(url, **kwargs) -> DataSpace",description:`Loads csv data in the main dataframe
`,long_description:null,example:null,params:{url:{description:`url of the csv file to load:
can be absolute if it starts with <tt class="docutils literal">/</tt>
or relative if it starts with <tt class="docutils literal">./</tt>
`,type:`<tt class="docutils literal">str</tt>
`,default:null},kwargs:{description:`keyword arguments to pass to Pandas
<tt class="docutils literal">read_csv</tt> function
`,type:null,default:null}},raises:{},return:{name:null,type:`<tt class="docutils literal">DataSpace</tt>
`}},Ct={funcdef:"def from_django(query) -> DataSpace",description:`Load the main dataframe from a django orm query
`,long_description:null,example:null,params:{query:{description:`django query from a model
`,type:`django query
`,default:null}},raises:{},return:{name:null,type:`<tt class="docutils literal">DataSpace</tt>
`}};var Dt={_load_csv:yt,_load_django:vt,from_df:bt,from_csv:xt,from_django:Ct};const St="return dataspace.from_df([1])",Tt=`ds = await load_dataset("bitcoin")
ds.show()`,Ft=`ds = await load_dataset("bitcoin")
print(ds.cols_())
ds.show()`,Et=`data = {"col1": [1, np.nan, 2, None, 3, 3]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
n = ds.count_null_("col1")
print("The column has", n, "nulls")
ds.show()`,At=`data = {"col1": ["foo", "", "bar", ""]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
n = ds.count_empty_("col1")
print("The column has", n, "empty values")
ds.show()`,Rt=`data = {"col1": [0, 1, 2, 0, 3, 3]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
n = ds.count_zero_("col1")
print("The column has", n, "zero values")
ds.show()`,Lt=`data = {"col1": [1, 2, 2, 3, 3, 3]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
n = ds.count_unique_("col1")
print("The column has", n, "unique values")
ds.show()`,kt=`data = {"col1": ["one", "two", "two", "three", "three", "three"]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
df = ds.wunique_("col1")
print("Dataframe of unique values weights:")
print(df)`,Bt=`df = pd.DataFrame(np.linspace(1, 100, 1000))
ds = dataspace.from_df(df)
print("Initial length:", len(ds.df.index))
ds.limit(10)
print("New length after limiting:", len(ds.df.index))
ds.show()`,Nt=`data = {"col1": ["A", "B", "C", "A", "B"]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
uv = ds.unique_("col1")
print("Colum unique values:", uv)
ds.show()`,Mt=`data = {"col1": [14, 8, np.nan], "col2": [2, np.nan, np.nan]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
print("The col1 has", ds.count_null_("col1"), "nulls")
ds.drop_nan("col1")
ds.show()`,qt=`data = {"col1": [14, 8, np.nan], "col2": [2, np.nan, np.nan]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.count_null_("col1")
ds.fill_nan("val", "col1")
ds.show()`,Ht=`data = {"col1": np.array([1, None, ""]), "col2": np.array([None, 0, None])}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.count_empty_("col1")
ds.count_null_("col1")
ds.fill_nulls()
ds.show()`,$t=`ds = await load_dataset("timeserie")
print(ds.df.head())
ds.fdate("date", precision="D")
ds.show()`,Ot=`ds = await load_dataset("bitcoin")
print("1. Initial dataframe:")
print(ds.df.head(1))
print("2. Colums:")
print(ds.cols_())
ds.to_date("ReceiptTS")
print("3. New column types:", ds.cols_())
ds.show()`,Pt=`ds = await load_dataset("timeserie")
print(ds.df.head())
ds.timestamps("date")
ds.show()`,Qt=`data = {"col1": ["5", "8", "3"], "col2": ["8", "7", "2"]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
print("Column types:", ds.cols_())
ds.to_int("col1", "col2")
print("Column types after convert:", ds.cols_())
ds.show()`,It=`data = {"col1": ["0.25", "0.85", "0.58"]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
print("Column types:", ds.cols_())
ds.to_float("col1")
print("Column types after convert:", ds.cols_())
ds.show()`,Ut=`data = {"col1": [1, 0, 0]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
print("Column types:", ds.cols_())
ds.to_type(bool, "col1")
print("Column types after convert:", ds.cols_())
ds.show()`,jt=`data = {"col1": [" one ", "two "]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
print(list(ds.df.col1))
ds.strip("col1")
print(list(ds.df.col1))
ds.show()`,Kt=`data = {"col1 ": [1, 2], " col2 ": [3, 4]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
print(list(ds.df.columns.values))
ds.strip_cols()
print(list(ds.df.columns.values))
ds.show()`,zt=`data = {"col1": [1.25889, 1.25874, 1.42587]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.roundvals("col1")
ds.show()`,Jt=`data = {"col1": ["a", "b", "novalue"]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.replace("col1", "novalue", "c")
ds.show()`,Vt=`data = {"col1": ["a", "b", "c"], "col2": [12, 7, 5]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.index("col1")
ds.show()`,Gt=`ds = await load_dataset("timeserie")
ds.dateindex("date")
ds.show()`,Xt=`ds = await load_dataset("bitcoin")
print("Unique values in the sources column:", ds.unique_("Source"))
dss = ds.split_("Source")
print("splitted DataSpace objects:", dss.keys())
dss["FTX"].show()`,Yt=`data = {"col1": ["A", "B", "C", "D"]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.indexcol("id")
ds.show()`,Wt=`data = {"col1": [14, 8, 12], "col2": [0, 1, 0]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.drop("col2")
ds.show()`,Zt=`df = pd.DataFrame(np.linspace(1, 100, 5), columns=["num"])
ds = dataspace.from_df(df)
print("Adding a column with default value")
ds.add("num2", 1)
ds.show()`,tn=`data = {"col1": [0, 1, 0]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.rename("col1", "new name")
ds.show()`,nn=`data = {"col1": [0, 1, 0], "col2": [0, 0, 1], "col3": [1, 1, 1], "col4": [0, 0, 1]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.keep("col1", "col4")
ds.show()`,en=`data = {"col1": [14, 8, 12], "col2": [0, 1, 0]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.copycol("col2", "new col name")
ds.show()`,an=`data = {"col1": [14, 25, 3, 8, 12]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.sort("col1")
ds.show()`,sn=`data = {"col1": [1, 0, 1, 4, 5, 1]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.exclude("col1", 1)
ds.show()`,dn=`data = {"col1": [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.dropr([0, 4])
ds.show()`,on=`data = {"col1": [1, 2], "col2": ["foo", "bar"]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.append(0, "baz")
ds.show()`,ln=`data = {"col1": [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.reverse()
ds.show()`,rn=`data = {"col1": [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)

def f(row):
    # add a new column with a value
    row["newcol"] = row["col1"] + 1
    return row

ds.apply(f)
ds.show()`,cn=`ds = await load_dataset("bitcoin")
ds.keep("mktTS", "qty")
ds.dateindex("mktTS")
ds.rsum("1S", "Datapoints per second")
ds.rename("qty", "Market volume")
ds.show()`,pn=`ds = await load_dataset("bitcoin")
ds.rmean("1S", "Datapoints per second", dateindex="mktTS")
ds.rename("px", "Mean price")
ds.show()`,un=`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.line_()`,fn=`data = {"col1": ["A", "B", "C", "D", "E"], "col2": [1, 6, 2, 4, 1]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
ds.bar_("col1:N", "col2:Q")`,mn=`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.line_()`,_n=`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.point_()`,hn=`ds = await load_dataset("sp500")
ds.axis("date:T", "price:Q")
ds.area_()`,wn=`data = {"col1": ["A", "B", "C", "D", "E"], "col2": [1, 6, 2, 4, 1]}
df = pd.DataFrame(data)
ds = dataspace.from_df(df)
chart = ds.bar_("col1:N", "col2:Q")
hline = ds.hline_(style={"color": "green"})
chart + hline`;var gn={load_dataset:St,show:Tt,cols_:Ft,count_null_:Et,count_empty_:At,count_zero_:Rt,count_unique_:Lt,wunique_:kt,limit:Bt,unique_:Nt,drop_nan:Mt,fill_nan:qt,fill_nulls:Ht,fdate:$t,to_date:Ot,timestamps:Pt,to_int:Qt,to_float:It,to_type:Ut,strip:jt,strip_cols:Kt,roundvals:zt,replace:Jt,index:Vt,dateindex:Gt,split_:Xt,indexcol:Yt,drop:Wt,add:Zt,rename:tn,keep:nn,copycol:en,sort:an,exclude:sn,dropr:dn,append:on,reverse:ln,apply:rn,rsum:cn,rmean:pn,axis:un,bar_:fn,line_:mn,point_:_n,area_:hn,hline_:wn};const yn={class:"text-xl"},vn={class:"mt-5"},bn={key:0},xn=e("div",{class:"p-5 pl-8 text-lg italic"},"Example",-1),Cn={key:0,class:"w-full p-3"},Fn=T({setup(t){const a=N({name:"",docstring:{}}),s=y(""),u=y({}),v=y(!1);function b(){var p,o,_;console.log("LOAD");const i=(p=C.currentRoute.value.params)==null?void 0:p.name;a.name="",v.value=!1,u.value={};let n;if(i)n=i.toString();else return;const c=(o=C.currentRoute.value.meta)==null?void 0:o.source;let d;c=="chart"?d=gt[n]:c=="toplevel"?d=Dt[n]:d=L[n],a.name=n,a.docstring=d,a.docstring.example?s.value=a.docstring.example:s.value=(_=gn[n])!=null?_:""}const f=F(()=>b());return M(()=>f()),(i,n)=>(l(),r(E,null,[e("div",yn," Method "+q(g(a).name),1),e("div",vn,[S(et,{method:g(a)},null,8,["method"])]),s.value.length>0?(l(),r("div",bn,[xn,g(a).name.length>0?(l(),r("div",Cn,[S(k,{id:g(a).name,code:s.value},null,8,["id","code"])])):h("",!0)])):h("",!0)],64))}});export{Fn as default};
