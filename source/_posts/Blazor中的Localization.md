---
title: Blazor中的Localization
categories:
  - 学习笔记
tags:
  - Blazor Localization
toc: true# 是否启用内容索引
---

[参考连接](https://code-maze.com/localization-in-blazor-webassembly-applications/)

### 1.根据浏览器语言显示语言
1. 项目中新建Resources文件夹
2. 新建Text.resx文件(这个不用加语言的后缀,会报错`自定义工具 PublicResXFileCodeGenerator 未能对输入文件产生输出`)
3. 新建其他语言的Text文件,比如Text.zh.resx
4. resx文件中访问修饰符需要设置`public`,每个文件中的名称需要相同,值是各个语言
![](https://image.yayan.xyz/20231009202818.png)
5. 完成之后,类似下图
![](https://image.yayan.xyz/20231009202906.png)

6. 在`Program.cs`中添加`builder.Services.AddLocalization();`
7. 在`_Imports.razor`中添加
   - `@using Microsoft.Extensions.Localization`
   - `@using 项目名.文件夹名称`,例如:`@using BlazorWasmLocalization.Shared.ResourceFiles`
8. 在页面中添加代码,其中Text就是resx文件的名称
```blazor
@page "/"
@inject IStringLocalizer<Text> localizer

<h1>@localizer["resx文件中的一个名称"]</h1>
@localizer["resx文件中的一个名称"]
```


### 2.根据用户选择的语言显示语言

1. 可以新建一个组件也可以直接在页面中添加
```blazor
<!-- 下拉选框 -->
<strong>Culture:</strong>

<select class="form-control" @bind="Culture" style="width:300px; margin-left:10px;">
    @foreach (var culture in cultures)
    {
        <option value="@culture">@culture.DisplayName</option>
    }
</select>

<!-- 组件代码 -->
public partial class CultureSelector
{
    [Inject]
    public NavigationManager NavManager { get; set; }

    [Inject]
    public IJSRuntime JSRuntime { get; set; }

    <!-- 语言列表,和resx文件对应 -->
    CultureInfo[] cultures = new[]
    {
        new CultureInfo("en-US"),
        new CultureInfo("zh-CN")
    };

    CultureInfo Culture
    {
        get => CultureInfo.CurrentCulture;
        set
        {
            if (CultureInfo.CurrentCulture != value)
            {
                var js = (IJSInProcessRuntime)JSRuntime;
                js.InvokeVoid("blazorCulture.set", value.Name);
                <!-- 每次选择之后会刷新一下页面 -->
                NavManager.NavigateTo(NavManager.Uri, forceLoad: true);
            }
        }
    }
}
```
2. 在项目下新建一个`Extensions`文件夹,新建一个`WebAssemblyHostExtension.cs`文件
```balzor
public static class WebAssemblyHostExtension
{
    public async static Task SetDefaultCulture(this WebAssemblyHost host)
    {
        var jsInterop = host.Services.GetRequiredService<IJSRuntime>();
        var result = await jsInterop.InvokeAsync<string>("blazorCulture.get");

        CultureInfo culture;

        if (result != null)
            culture = new CultureInfo(result);
        else
            culture = new CultureInfo("zh-CN");

        CultureInfo.DefaultThreadCurrentCulture = culture;
        CultureInfo.DefaultThreadCurrentUICulture = culture;
    }
}
```

3. 在`Program.cs`中添加
```blazor
var host = builder.Build();
await host.SetDefaultCulture();
await host.RunAsync();
``` 
4. 在`wwwroot/index.html`中添加
```html
<script>
       blazorCulture = {
            get: () => localStorage['BlazorCulture'],
            set: (value) => localStorage['BlazorCulture'] = value
        };
    </script>
```

5. 在csproj文件中添加
```xml
 <BlazorWebAssemblyLoadAllGlobalizationData>true</BlazorWebAssemblyLoadAllGlobalizationData>
 ```

6. 运行即可










