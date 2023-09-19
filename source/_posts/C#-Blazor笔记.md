
---
title: Blazor学习笔记
categories:
  - 学习笔记
tags:
  - Blazor
toc: true# 是否启用内容索引
---
😍😍😍

## Blazor

用C#代替JavaScript创建丰富的UI


## 页面组件

### 组件

> 1. 以razor结尾,文件名首字母大写,HTML和C#代码的组合.
> 2. 类似vue,在组件中可以使用@来引用变量

```C#
<h1 style="font-style:@_headingFontStyle">@_headingText</h1>

@code {
    private string _headingFontStyle = "italic";
    private string _headingText = "你好,世界!";
}

```

### 组件参数

> 1. 定义一个带有[Parameter]的公共属性,在父类使用这个组件时,可以传参

```C#
// 子组件:Child
<h1>@Title</h1>

@code {
    [Parameter]
    public string Title { get; set; }
}


// 父组件
<Child Title="传递参数" />
```

### 组件多参数

> 1. 当子组件可携带多个参数时,不用每个参数都进行定义.
> 2. 使用@attributes语法关联字段进行绑定

```C#
// 第一种方式,单独传参
<input title="@Title" value="@Value"  />

// 第二种方式,attribute字典传参
<input @attributes="ButtonAttributes" />


@code {
    [Parameter]
    public string Title { get; set; } = "Hello";

    [Parameter]
    public string Value { get; set; } = "10";

    [Parameter]
    public Dictionary<string, object> ButtonAttributes { get; set; } = new Dictionary<string, object>()
{
        { "title","Hello" } ,
        { "value","10" } ,
    };
}

```
---

## 组件生命周期


---

## 组件模板

> 1. 父组件在使用子组件时，可以向子组件中插入代码片段.类似vue中的插槽?

```c#

// 子组件，构建一个RenderFragment模板
@typeparam IData
<table>

    <thead>
        @HeaderTemplate
    </thead>
    <tbody>
        @foreach (var item in Data)
        {
            <tr>

                <td>@RowTemplate(item)</td>
            </tr>
        }
    </tbody>

</table>

@code {

    [Parameter]
    public RenderFragment HeaderTemplate { get; set; }

    [Parameter]
    public RenderFragment<IData> RowTemplate { get; set; }

    [Parameter]
    public IReadOnlyList<IData> Data { get; set; }
}
// 父组件使用时传递html标签
<TableTemplate Data="students">
    <HeaderTemplate>
        <th>Id</th>
        <th>Name</th>
    </HeaderTemplate>

    <RowTemplate>
        <td>@context.Id</td>
        <td>@context.Name</td>
    </RowTemplate>
</TableTemplate>
@code{
    public List<Student> students { get; set; }

    protected override Task OnInitializedAsync()
    {
        students = new List<Student>();
        students.Add(new Student() { Id = 1, Name = "John" });
        students.Add(new Student() { Id = 2, Name = "Mary" });
        students.Add(new Student() { Id = 3, Name = "Jane" });
        students.Add(new Student() { Id = 4, Name = "Peter" });
        return base.OnInitializedAsync();

    }
}

```

---

## 组件方法

> 1. 子组件时间完成之后的一个回调,当子组件发生某个事件之后通知父组件，父组件的一个响应函数
> 2. 下面的例子，当子组件发生点击事件之后，父组件可做出相应的反应

```C#
// 子组件：ChildCallBack

<button @onclick="OnClickChild">
       Click
</button>

@code {
    [Parameter]
    public EventCallback<MouseEventArgs> OnClickCallback { get; set; }

    // 
     private async void OnClickChild(){
        // do somethings

        // ()传递参数
        OnClickCallback.InvokeAsync(1);

     }
}

// 父组件
<ChildCallBack OnClickCallback="ReceiveDataFromSideBar"></ChildCallBack>

@code{
     private void ReceiveDataFromSideBar(int number)
        {
            // 可接受参数做处理
        }
}

```

---

## 事件处理

> 1. 在标签中使用@绑定一个事件，一种使用lambda表达式直接处理，一种使用函数

```C#

// 1.lambda
<input @onchange="@(()=>Console.WriteLine("Hello"))" />
<button @onclick="@(()=>Console.WriteLine("Hello"))" />

// 2.@code中使用函数

<button @onclick="Show" />
@code
{
    public void Show()
    {
       //当按钮被点击, 将执行下面代码
    }
}


// 3.携带事件参数，在默认的情况下, 我们如果只编写一个事件触发的方法, 并且明确它是否有参数, 在UI元素绑定方法上, 我们都无需传递参数
<button @onclick="Show" />
@code{
    public async Task Show(MouseEventArgs  e)
    {
        //...
    }
}

// 4.可重载，带有事件或不带事件
<button @onclick="@(e=>Show(e))" />  //调用带事件参数的方法
<button @onclick="@(()=>Show())" />  //调用不带事件参数的方法
@code
{
    //不带事件参数的方法
    public void Show()
    {

    }

    //带事件参数的方法
    public void Show(MouseEventArgs e)
    {

    }
}

```

---

## 数据绑定

### 绑定字段

> 1. 类似vue中的v-bind，可以绑定C#字段,双向绑定
> 2. @xxx和@bind的区别：value="@xxx": 只能做到属性呈现到UI元素当中, 元素发生变化并不会影响到属性变更。

```C#
<input @bind="Name" />

@code {
    private string Name{ get; set; }
}


```

### 绑定对象的属性

```c#
<input @bind="Stu.Name"/>

@code{
    public Student Stu { get; set; } = new Student()
    {
        Name = "123"
    };

    public class Student
    {
        public string Name { get; set; }
    }
}


```

### 绑定数据格式化

```c#
<input @bind="StartDate" @bind:format="yyyy-MM-dd" />

@code {
    [Parameter]
    public DateTime StartDate { get; set; } = new DateTime(2020, 1, 1);
}


```

### 父组件参数绑定到子组件

> 1. 当父组件的参数改变时，子组件中的参数也会同时改变

```c#
// ChildComponent 
<p>Year: @Year</p>

@code {
    [Parameter]
    public int Year { get; set; }

    [Parameter]
    public EventCallback<int> YearChanged { get; set; }
}



// 父组件
<ChildComponent @bind-Year="ParentYear" />

<input @bind="ParentYear" />

@code {
    [Parameter]
    public int ParentYear { get; set; } = 1978;

}

```

---

## 路由和页面导航

> 1. @page "/xxx" 组件的路由
> 2. @page "/xxx/{aaa}"  aaa是路由传参，在@code中添加一个公共字段aaa，
> 3. @page "/xxx/{aaa:int}"  指定参数类型
> 4. NavigationManager.NavigateTo("/test/999"); 跳转页面(NavLink 也可以)



---

## Blazor Server和Blazor WebAssembly

[官网说明](https://learn.microsoft.com/zh-cn/aspnet/core/blazor/hosting-models?view=aspnetcore-7.0)
>服务器把东西全部运行在浏览器的沙盒里,
- Blazor WebAssembly的优点
  - 在浏览器中执行C#代码，不需要额外的插件
  - 可以基于WebAssembly的性能优势和可在浏览器内执行的能力，获得更快页面处理速度
  - 支持无服务器和离线场景
- Blazor WebAssembl的缺点
  - 需要加载太多资源，首次展现速度较慢
  - 由于所有代码都在浏览器中执行，不能嵌入机密数据


>Blazor Server类似MVC,但是Server是长连接,在服务器端计算结果差异,浏览器拿到差异渲染(blazor.server.js)
- Blazor Server的优点
  - 页面加载是轻量级的
  - 服务器可以使用机密数据，例如访问数据库
  - 它支持100%的浏览器，即使是那些没有WASM支持的浏览器，如Internet Explorer。
- Blazor Server的缺点
  - 需要一个http://ASP.NET Core服务器
  - 不支持无服务器和离线场景
  - 大量SignalR连接可能引发性能问题,保持连接
