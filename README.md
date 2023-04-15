# Dataspace

[![pub package](https://img.shields.io/pypi/v/dataspace)](https://pypi.org/project/dataspace/) [![Coverage Status](https://coveralls.io/repos/github/synw/dataspace/badge.svg?branch=main)](https://coveralls.io/github/synw/dataspace?branch=main)

A simple api to explore, clean, transform and visualize data

## Features

- **Explore data**: describe, search and visualize raw data
- **Clean and transform data**: select, filter, normalize and reshape data
- **Visualize data**: many kind of charts

<details>
<summary>:books: Read the <a href="https://synw.github.io/dataspace">documentation</a></summary>

 - [Doc](https://synw.github.io/dataspace/doc)
     - [Data io](https://synw.github.io/dataspace/doc/data_io)
         - [Load](https://synw.github.io/dataspace/doc/data_io/load)
            - [From df](https://synw.github.io/dataspace/doc/data_io/load/from_df)
            - [From csv](https://synw.github.io/dataspace/doc/data_io/load/from_csv)
            - [From django](https://synw.github.io/dataspace/doc/data_io/load/from_django)
         - [Export](https://synw.github.io/dataspace/doc/data_io/export)
            - [Export csv](https://synw.github.io/dataspace/doc/data_io/export/export_csv)
     - [Infos](https://synw.github.io/dataspace/doc/infos)
         - [View data](https://synw.github.io/dataspace/doc/infos/view_data)
            - [Show](https://synw.github.io/dataspace/doc/infos/view_data/show)
         - [Count data](https://synw.github.io/dataspace/doc/infos/count_data)
            - [Count null ](https://synw.github.io/dataspace/doc/infos/count_data/count_null_)
            - [Count zero ](https://synw.github.io/dataspace/doc/infos/count_data/count_zero_)
            - [Count unique ](https://synw.github.io/dataspace/doc/infos/count_data/count_unique_)
            - [Wunique ](https://synw.github.io/dataspace/doc/infos/count_data/wunique_)
     - [Select](https://synw.github.io/dataspace/doc/select)
        - [Limit](https://synw.github.io/dataspace/doc/select/limit)
        - [Unique ](https://synw.github.io/dataspace/doc/select/unique_)
     - [Clean](https://synw.github.io/dataspace/doc/clean)
         - [Nulls](https://synw.github.io/dataspace/doc/clean/nulls)
            - [Drop na](https://synw.github.io/dataspace/doc/clean/nulls/drop_na)
            - [Drop any nulls](https://synw.github.io/dataspace/doc/clean/nulls/drop_any_nulls)
            - [Drop all nulls](https://synw.github.io/dataspace/doc/clean/nulls/drop_all_nulls)
            - [Fill nulls](https://synw.github.io/dataspace/doc/clean/nulls/fill_nulls)
         - [Dates](https://synw.github.io/dataspace/doc/clean/dates)
            - [To date](https://synw.github.io/dataspace/doc/clean/dates/to_date)
            - [To tzdate](https://synw.github.io/dataspace/doc/clean/dates/to_tzdate)
            - [Fdate](https://synw.github.io/dataspace/doc/clean/dates/fdate)
            - [Timestamps](https://synw.github.io/dataspace/doc/clean/dates/timestamps)
         - [Convert types](https://synw.github.io/dataspace/doc/clean/convert_types)
            - [To int](https://synw.github.io/dataspace/doc/clean/convert_types/to_int)
            - [To float](https://synw.github.io/dataspace/doc/clean/convert_types/to_float)
            - [To str](https://synw.github.io/dataspace/doc/clean/convert_types/to_str)
            - [To type](https://synw.github.io/dataspace/doc/clean/convert_types/to_type)
         - [Clean values](https://synw.github.io/dataspace/doc/clean/clean_values)
            - [Strip](https://synw.github.io/dataspace/doc/clean/clean_values/strip)
            - [Strip cols](https://synw.github.io/dataspace/doc/clean/clean_values/strip_cols)
            - [Roundvals](https://synw.github.io/dataspace/doc/clean/clean_values/roundvals)
            - [Replace](https://synw.github.io/dataspace/doc/clean/clean_values/replace)
     - [Transform](https://synw.github.io/dataspace/doc/transform)
         - [Dataframe](https://synw.github.io/dataspace/doc/transform/dataframe)
            - [Split ](https://synw.github.io/dataspace/doc/transform/dataframe/split_)
            - [Drop](https://synw.github.io/dataspace/doc/transform/dataframe/drop)
            - [Add](https://synw.github.io/dataspace/doc/transform/dataframe/add)
            - [Rename](https://synw.github.io/dataspace/doc/transform/dataframe/rename)
            - [Keep](https://synw.github.io/dataspace/doc/transform/dataframe/keep)
            - [Copycol](https://synw.github.io/dataspace/doc/transform/dataframe/copycol)
            - [Reverse](https://synw.github.io/dataspace/doc/transform/dataframe/reverse)
         - [Values](https://synw.github.io/dataspace/doc/transform/values)
            - [Sort](https://synw.github.io/dataspace/doc/transform/values/sort)
            - [Exclude](https://synw.github.io/dataspace/doc/transform/values/exclude)
            - [Append](https://synw.github.io/dataspace/doc/transform/values/append)
            - [Mappend](https://synw.github.io/dataspace/doc/transform/values/mappend)
            - [Diffm](https://synw.github.io/dataspace/doc/transform/values/diffm)
         - [Resample timeseries](https://synw.github.io/dataspace/doc/transform/resample_timeseries)
            - [Resample](https://synw.github.io/dataspace/doc/transform/resample_timeseries/resample)
            - [Rsum](https://synw.github.io/dataspace/doc/transform/resample_timeseries/rsum)
            - [Rmean](https://synw.github.io/dataspace/doc/transform/resample_timeseries/rmean)
         - [Calculations](https://synw.github.io/dataspace/doc/transform/calculations)
            - [Percent](https://synw.github.io/dataspace/doc/transform/calculations/percent)
            - [Diffp](https://synw.github.io/dataspace/doc/transform/calculations/diffp)
            - [Diffpp](https://synw.github.io/dataspace/doc/transform/calculations/diffpp)
            - [Diffn](https://synw.github.io/dataspace/doc/transform/calculations/diffn)
            - [Diffnp](https://synw.github.io/dataspace/doc/transform/calculations/diffnp)
            - [Diffm](https://synw.github.io/dataspace/doc/transform/calculations/diffm)
            - [Diffmp](https://synw.github.io/dataspace/doc/transform/calculations/diffmp)
            - [Cvar ](https://synw.github.io/dataspace/doc/transform/calculations/cvar_)
            - [Lreg ](https://synw.github.io/dataspace/doc/transform/calculations/lreg_)
     - [Charts](https://synw.github.io/dataspace/doc/charts)
         - [Options](https://synw.github.io/dataspace/doc/charts/options)
            - [Axis](https://synw.github.io/dataspace/doc/charts/options/axis)
            - [Altair](https://synw.github.io/dataspace/doc/charts/options/altair)
            - [Bokeh](https://synw.github.io/dataspace/doc/charts/options/bokeh)
            - [W](https://synw.github.io/dataspace/doc/charts/options/w)
            - [H](https://synw.github.io/dataspace/doc/charts/options/h)
            - [Wh](https://synw.github.io/dataspace/doc/charts/options/wh)
         - [Draw charts](https://synw.github.io/dataspace/doc/charts/draw_charts)
            - [Line ](https://synw.github.io/dataspace/doc/charts/draw_charts/line_)
            - [Point ](https://synw.github.io/dataspace/doc/charts/draw_charts/point_)
            - [Bar ](https://synw.github.io/dataspace/doc/charts/draw_charts/bar_)
            - [Area ](https://synw.github.io/dataspace/doc/charts/draw_charts/area_)
            - [Square ](https://synw.github.io/dataspace/doc/charts/draw_charts/square_)
            - [Rule ](https://synw.github.io/dataspace/doc/charts/draw_charts/rule_)
            - [Tick ](https://synw.github.io/dataspace/doc/charts/draw_charts/tick_)
            - [Bar num ](https://synw.github.io/dataspace/doc/charts/draw_charts/bar_num_)
            - [Line num ](https://synw.github.io/dataspace/doc/charts/draw_charts/line_num_)
            - [Point num ](https://synw.github.io/dataspace/doc/charts/draw_charts/point_num_)
            - [Heatmap ](https://synw.github.io/dataspace/doc/charts/draw_charts/heatmap_)
            - [Hist ](https://synw.github.io/dataspace/doc/charts/draw_charts/hist_)
            - [Hline ](https://synw.github.io/dataspace/doc/charts/draw_charts/hline_)
         - [Inline api](https://synw.github.io/dataspace/doc/charts/inline_api)
            - [W](https://synw.github.io/dataspace/doc/charts/inline_api/w)
            - [H](https://synw.github.io/dataspace/doc/charts/inline_api/h)
            - [Wh](https://synw.github.io/dataspace/doc/charts/inline_api/wh)
            - [Mw](https://synw.github.io/dataspace/doc/charts/inline_api/mw)
            - [Pw](https://synw.github.io/dataspace/doc/charts/inline_api/pw)
            - [Color](https://synw.github.io/dataspace/doc/charts/inline_api/color)
            - [Opacity](https://synw.github.io/dataspace/doc/charts/inline_api/opacity)
            - [Tooltip](https://synw.github.io/dataspace/doc/charts/inline_api/tooltip)
            - [To](https://synw.github.io/dataspace/doc/charts/inline_api/to)
            - [Rx](https://synw.github.io/dataspace/doc/charts/inline_api/rx)
            - [Nox](https://synw.github.io/dataspace/doc/charts/inline_api/nox)
            - [Noy](https://synw.github.io/dataspace/doc/charts/inline_api/noy)
            - [Title](https://synw.github.io/dataspace/doc/charts/inline_api/title)
            - [Colormap](https://synw.github.io/dataspace/doc/charts/inline_api/colormap)
            - [Qcolormap](https://synw.github.io/dataspace/doc/charts/inline_api/qcolormap)
            - [Save img](https://synw.github.io/dataspace/doc/charts/inline_api/save_img)
            - [Get html ](https://synw.github.io/dataspace/doc/charts/inline_api/get_html_)
            - [Html header ](https://synw.github.io/dataspace/doc/charts/inline_api/html_header_)
     - [Reporting](https://synw.github.io/dataspace/doc/reporting)
         - [Prepare a report](https://synw.github.io/dataspace/doc/reporting/prepare_a_report)
            - [Report path](https://synw.github.io/dataspace/doc/reporting/prepare_a_report/report_path)
            - [Stack](https://synw.github.io/dataspace/doc/reporting/prepare_a_report/stack)
         - [Export](https://synw.github.io/dataspace/doc/reporting/export)
            - [Save pdf](https://synw.github.io/dataspace/doc/reporting/export/save_pdf)
            - [Save html](https://synw.github.io/dataspace/doc/reporting/export/save_html)

</details>

This api is:

- *Minimalistic*: short names, simple functionalites, minimal parameters
- *Pragmatic*: focuses on raw efficiency rather than strictly idiomatic code while favouring static typing
- *Simple stupid*: keep it easy to understand for both code and api

## Install

```
pip install dataspace
```

Optional: to use the Bokeh chart engine:

```
pip install bokeh holoviews
```

Note: the Pandas dependency is required for this chart engine as it does 
not yet support Polars dataframes

## Dependencies

- Dataframe: [Polars](https://github.com/pola-rs/polars)
- Charts: [Altair](https://github.com/altair-viz/altair), and [Holoviews](https://github.com/holoviz/holoviews) with [Bokeh](https://github.com/bokeh/bokeh) (optional)

## Example notebooks

[Example notebooks](https://github.com/synw/dataspace_notebooks) are available

[![badge](https://img.shields.io/badge/launch-notebooks-579ACA.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFkAAABZCAMAAABi1XidAAAB8lBMVEX///9XmsrmZYH1olJXmsr1olJXmsrmZYH1olJXmsr1olJXmsrmZYH1olL1olJXmsr1olJXmsrmZYH1olL1olJXmsrmZYH1olJXmsr1olL1olJXmsrmZYH1olL1olJXmsrmZYH1olL1olL0nFf1olJXmsrmZYH1olJXmsq8dZb1olJXmsrmZYH1olJXmspXmspXmsr1olL1olJXmsrmZYH1olJXmsr1olL1olJXmsrmZYH1olL1olLeaIVXmsrmZYH1olL1olL1olJXmsrmZYH1olLna31Xmsr1olJXmsr1olJXmsrmZYH1olLqoVr1olJXmsr1olJXmsrmZYH1olL1olKkfaPobXvviGabgadXmsqThKuofKHmZ4Dobnr1olJXmsr1olJXmspXmsr1olJXmsrfZ4TuhWn1olL1olJXmsqBi7X1olJXmspZmslbmMhbmsdemsVfl8ZgmsNim8Jpk8F0m7R4m7F5nLB6jbh7jbiDirOEibOGnKaMhq+PnaCVg6qWg6qegKaff6WhnpKofKGtnomxeZy3noG6dZi+n3vCcpPDcpPGn3bLb4/Mb47UbIrVa4rYoGjdaIbeaIXhoWHmZYHobXvpcHjqdHXreHLroVrsfG/uhGnuh2bwj2Hxk17yl1vzmljzm1j0nlX1olL3AJXWAAAAbXRSTlMAEBAQHx8gICAuLjAwMDw9PUBAQEpQUFBXV1hgYGBkcHBwcXl8gICAgoiIkJCQlJicnJ2goKCmqK+wsLC4usDAwMjP0NDQ1NbW3Nzg4ODi5+3v8PDw8/T09PX29vb39/f5+fr7+/z8/Pz9/v7+zczCxgAABC5JREFUeAHN1ul3k0UUBvCb1CTVpmpaitAGSLSpSuKCLWpbTKNJFGlcSMAFF63iUmRccNG6gLbuxkXU66JAUef/9LSpmXnyLr3T5AO/rzl5zj137p136BISy44fKJXuGN/d19PUfYeO67Znqtf2KH33Id1psXoFdW30sPZ1sMvs2D060AHqws4FHeJojLZqnw53cmfvg+XR8mC0OEjuxrXEkX5ydeVJLVIlV0e10PXk5k7dYeHu7Cj1j+49uKg7uLU61tGLw1lq27ugQYlclHC4bgv7VQ+TAyj5Zc/UjsPvs1sd5cWryWObtvWT2EPa4rtnWW3JkpjggEpbOsPr7F7EyNewtpBIslA7p43HCsnwooXTEc3UmPmCNn5lrqTJxy6nRmcavGZVt/3Da2pD5NHvsOHJCrdc1G2r3DITpU7yic7w/7Rxnjc0kt5GC4djiv2Sz3Fb2iEZg41/ddsFDoyuYrIkmFehz0HR2thPgQqMyQYb2OtB0WxsZ3BeG3+wpRb1vzl2UYBog8FfGhttFKjtAclnZYrRo9ryG9uG/FZQU4AEg8ZE9LjGMzTmqKXPLnlWVnIlQQTvxJf8ip7VgjZjyVPrjw1te5otM7RmP7xm+sK2Gv9I8Gi++BRbEkR9EBw8zRUcKxwp73xkaLiqQb+kGduJTNHG72zcW9LoJgqQxpP3/Tj//c3yB0tqzaml05/+orHLksVO+95kX7/7qgJvnjlrfr2Ggsyx0eoy9uPzN5SPd86aXggOsEKW2Prz7du3VID3/tzs/sSRs2w7ovVHKtjrX2pd7ZMlTxAYfBAL9jiDwfLkq55Tm7ifhMlTGPyCAs7RFRhn47JnlcB9RM5T97ASuZXIcVNuUDIndpDbdsfrqsOppeXl5Y+XVKdjFCTh+zGaVuj0d9zy05PPK3QzBamxdwtTCrzyg/2Rvf2EstUjordGwa/kx9mSJLr8mLLtCW8HHGJc2R5hS219IiF6PnTusOqcMl57gm0Z8kanKMAQg0qSyuZfn7zItsbGyO9QlnxY0eCuD1XL2ys/MsrQhltE7Ug0uFOzufJFE2PxBo/YAx8XPPdDwWN0MrDRYIZF0mSMKCNHgaIVFoBbNoLJ7tEQDKxGF0kcLQimojCZopv0OkNOyWCCg9XMVAi7ARJzQdM2QUh0gmBozjc3Skg6dSBRqDGYSUOu66Zg+I2fNZs/M3/f/Grl/XnyF1Gw3VKCez0PN5IUfFLqvgUN4C0qNqYs5YhPL+aVZYDE4IpUk57oSFnJm4FyCqqOE0jhY2SMyLFoo56zyo6becOS5UVDdj7Vih0zp+tcMhwRpBeLyqtIjlJKAIZSbI8SGSF3k0pA3mR5tHuwPFoa7N7reoq2bqCsAk1HqCu5uvI1n6JuRXI+S1Mco54YmYTwcn6Aeic+kssXi8XpXC4V3t7/ADuTNKaQJdScAAAAAElFTkSuQmCC)](https://mybinder.org/v2/gh/synw/dataspace_notebooks/HEAD)

```
├── chart
│   ├── area
│   ├── bar
│   ├── hline
│   ├── line
│   └── point
├── clean
│   ├── convert
│   ├── date
│   ├── drop_nulls
│   ├── fill_nulls
│   ├── strip
│   └── values
├── count
│   ├── count_empty
│   ├── count_null
│   ├── count_unique
│   └── count_zero
├── io
│   ├── export
│   └── load
├── select
│   ├── limit
│   ├── unique
│   └── wunique
└── transform
    ├── dataframe
    │   ├── add
    │   ├── copycol
    │   ├── drop
    │   ├── keep
    │   ├── rename
    │   └── split
    ├── diff
    │   ├── diffm
    │   ├── diffmp
    │   ├── diffn
    │   ├── diffnp
    │   ├── diffp
    │   └── diffpp
    ├── resample
    │   ├── rmean
    │   └── rsum
    └── values
        ├── append
        ├── exclude
        ├── reverse
        └── sort
```

## Tests

To run the tests:

```bash
make test
```


