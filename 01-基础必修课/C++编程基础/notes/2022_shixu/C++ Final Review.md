
# 9. 类和封装 (Encapsulation)

## 成员函数

成员函数在类定义中声明，它的具体实现（定义）可以放在类定义之外。但是成员函数的实现也可以放在类定义内，编译器会尝试将其视为内联函数 `inline calls`。

**内联函数**是一种优化手段。当编译器遇到内联函数的调用时，它会尝试将函数的代码直接插入到调用点，而不是进行常规的函数调用（压栈、跳转、出栈等）。这可以减少函数调用的开销，提高程序执行效率。但需要注意的是，`inline` 只是对编译器的一种“建议”，编译器可能会根据具体情况决定是否真正进行内联。对于大型函数或递归函数，编译器通常不会进行内联。

## `Block Scope & Class Scope` 类作用域和块作用域

如果一个成员函数内部定义了一个局部变量（具有块作用域），而这个局部变量的名字又恰好与类的某个成员变量（具有类作用域）的名字相同，那么在**该成员函数内部**，这个具有块作用域的局部变量会“隐藏”掉（`hidden`）同名的类作用域变量。
**当局部变量和成员变量同名时，局部变量优先**，但是可以加上 `ClassName::` 来访问类的成员变量。

## 构造函数、拷贝构造函数与析构函数、对象赋值（Memberwise Assignment）


**构造函数 (Constructor)**
- 可以有多个，形成重载，重载构造函数可以满足不同对象多参数的需要。
- 没有返回类型，函数名与类名相同，**参数列表向左对齐**。（需要3个参数但只给了一个，那么这一个参数就会先满足第一个）
- 如果在构造函数中调用类内的成员函数来初始化，很可能会导致逻辑错误因为数据成员还没有被正确初始化。

构造函数的参数列表是类对象例如 `string` `ClassOne` 等时，需要加上 `const` 关键字：
- 防止意外修改源对象；
- 提高函数通用性（接受右值），非 `const` 引用不能绑定到右值，即以下操作是错误的。
```cpp
class Person{
	private:
		string name;
	public:
		Person(string& n):name(n){...} // 错误！非const引用不能作为右值传递给name
		Person(const string& n):name(n){...} // 正确，const引用可以正常传递
};
```

**拷贝构造函数 (Copy Constructor)**

- 调用场景：对象初始化、值传递、返回对象。
- 默认拷贝构造为浅拷贝，自定义实现深拷贝。

```cpp
class MyArray {
public:
    int* ptr;
    int size;
    MyArray(int s) : size(s), ptr(new int[s]) {}
    MyArray(const MyArray& ArrayToCopy) : 
    size(ArrayToCopy.size), ptr(new int[ArrayToCopy.size]) {
        for (size_t i = 0; i < size; i++){
	        ptr[i] = ArrayToCopy.ptr[i];
        }
    }
    ~MyArray() { delete[] ptr; }
};
```

对象可以作为函数参数传递，也可以从函数返回。
对于每个类，编译器都提供了⼀个默认的复制构造函数，⽤于将原始对象的每个成员复制到新对象的相应成员中。
拷贝函数必须要**接收对象的引用**作为参数，不然可能会造成在调用拷贝构造函数时，先为这个参数创建一个副本。而创建这个副本又需要调用拷贝构造函数，这就形成了一个无限递归的循环，最终会导致栈溢出。并且为了保证引用所知对象不被修改，最好添加 `const` 关键字来保证。

**委托构造函数（Delegating constructor）** 
调⽤构造函数称为委托构造函数，它将其⼯作委托给另⼀个构造函数。
```cpp
Time::Time()
    : Time( 0, 0, 0 ) // delegate to Time( int, int, int )
{
    // end constructor with no arguments
}

Time::Time( int hour )
    : Time( hour, 0, 0 ) // delegate to Time( int, int, int )
{
    // end constructor with one argument
}

Time::Time( int hour, int minute )
    : Time( hour, minute, 0 ) // delegate to Time( int, int, int )
{
    // end constructor with two arguments
}
```

**析构函数 (Destructor)**
- 一个类只有一个，不能重载，没有参数，没有返回类型，不能加 `const` 。
- 如果没有显式定义，编译器默认添加析构函数。
- 调用顺序与构造函数逆序，全局对象和静态对象将按其创建的相反顺序销毁。派生类先，基类后。局部程序退出时也将调用析构函数。
- 建议基类析构函数声明为 `virtual`，以避免通过基类指针删除派生类对象时产生资源泄漏。

**对象的作用域 `scope` 和存储类型 `storage class` 可以更改构造函数和析构函数的调⽤顺序。**

```cpp
#include<iostream>
using namespace std;

CreateAndDestroy first( 1, "(global before main)" ); // global object

void create() {
    std::cout << "CREATE FUNCTION: EXECUTION BEGINS" << std::endl;
    
    CreateAndDestroy fifth(5, "(local automatic in create)");
    
    static CreateAndDestroy sixth(6, "(local static in create)");
    
    CreateAndDestroy seventh(7, "(local automatic in create)");
    
    std::cout << "CREATE FUNCTION: EXECUTION ENDS" << std::endl;
}

int main() {
    std::cout << "MAIN FUNCTION: EXECUTION BEGINS" << std::endl;
    
    CreateAndDestroy second(2, "(local automatic in main)");
    
    static CreateAndDestroy third(3, "(local static in main)");
    
    create(); //非静态的5，7在 create 函数结束时被释放
    
    std::cout << "MAIN FUNCTION: EXECUTION RESUMES" << std::endl;
    
    CreateAndDestroy fourth(4, "(local automatic in main)");
    
    std::cout << "MAIN FUNCTION: EXECUTION ENDS" << std::endl;
    
    return 0;
}
```
输出结果：（把全局/静态和非全局/main的量分开写）
```cpp
Object 1  constructor runs    (global before main)

MAIN FUNCTION: EXECUTION BEGINS
Object 2  constructor runs    (local automatic in main)
Object 3  constructor runs    (local static in main)

CREATE FUNCTION: EXECUTION BEGINS
Object 5  constructor runs    (local automatic in create)
Object 6  constructor runs    (local static in create)
Object 7  constructor runs    (local automatic in create)

CREATE FUNCTION: EXECUTION ENDS
Object 7  destructor runs    (local automatic in create)
Object 5  destructor runs    (local automatic in create)

MAIN FUNCTION: EXECUTION RESUMES
Object 4  constructor runs    (local automatic in main)

MAIN FUNCTION: EXECUTION ENDS
Object 4  destructor runs    (local automatic in main)
Object 2  destructor runs    (local automatic in main)
Object 6  destructor runs    (local static in create)
Object 3  destructor runs    (local static in main)
Object 1  destructor runs    (global before main)
```

**对象赋值（Memberwise Assignment）**

可以使用`=`将一个对象的值赋给另一个**相同类型**的对象。
例如，如果你有两个`MyClass`类型的对象`objA`和`objB`，你可以写 `objA = objB`；

- 当你不为你的类自定义赋值运算符时，C++编译器会为你生成一个默认的赋值运算符。这个默认的运算符执行的是“逐成员赋值”（memberwise assignment）。将源对象（赋值运算符右侧的对象）的每一个数据成员都会被单独复制并赋值给目标对象（赋值运算符左侧的对象）中对应的同名数据成员。
- 但是，如果一个类的数据成员包含**指向动态分配内存的指针**，默认的逐成员赋值就可能导致严重问题：
	- **浅拷贝问题（Shallow Copy）**：默认的赋值运算符只会复制指针本身的值（即内存地址），而不会复制指针指向的内存内容。这意味着赋值后，两个对象的指针会指向同一块动态内存。
	- **双重释放（Double Free）**：当其中一个对象超出作用域或被销毁时，它会释放这块共享的内存。如果另一个对象也尝试释放这块内存，就会导致程序崩溃（双重释放错误）。
	- **数据损坏（Data Corruption）**：如果一个对象通过其指针修改了这块共享内存的内容，另一个对象也会看到这些修改，这可能不是你期望的行为。


## `const` 常量成员函数

在成员函数后添加 `const` 表示常量成员函数。
- 不允许修改对象的非 `mutable` 数据成员。（ `mutable` 类型的数据成员后必须要加上相应的数据类型，例如 `mutable int a;`）
- 常量对象只能调用常量成员函数。

```cpp
class Point {
public:
    int x, y;
    Point(int x, int y) : x(x), y(y) {}
    void setX(int val) { x = val; }
    void getX() const { std::cout << "X: " << x << std::endl; }
};

int main() {
    const Point p1(1, 2);
    Point p2(3, 4);
    p1.setX(10); //错误！p1为const对象，不能调用非const成员函数setX
    p2.setX(30);
    p2.getX();
    return 0;
}
```

## 异常处理 (Exception Handling)

使用 `try-catch-throw` 块分离正常逻辑和错误处理。

## 组合 (Composition)

表示 has‑a 关系，类包含另一个类的对象作为成员。（车辆和引擎的关系就是很好的例子）
`Engine` can be considered as a **Composition** in `Car`!
```cpp
class Engine {
public:
    Engine(int hp = 1000) { std::cout << "Engine created with " << hp << " HP." << std::endl; }
    ~Engine() { std::cout << "Engine destroyed." << std::endl; }
};

class Car {
public:
    Car(const std::string& model, int hp) : modelName(model), engine(hp) {
        std::cout << "Car '" << modelName << "' created." << std::endl;
    }
    ~Car() { std::cout << "Car '" << modelName << "' destroyed." << std::endl; }
private:
    std::string modelName;
    Engine engine;
};
```

## `Friend` 友元函数或友元类

将 `classTwo` 声明为 `classOne` 的友元类：
```cpp
friend class classTwo
```
或者声明为友元函数，友元有权访问类中的全部数据成员。但是友元是授予的，不是接受。A要成为B的朋友就必须由B声明A为他的朋友。并且友元不可传递，不具有对称性。
友元函数*可以重载*，并且有些时候必须重载来满足程序要求。
## 静态数据成员 (Static Data Members)

- 属于类本身，所有对象共享。可以通过类作用域解析符 `::` 来访问，也可以通过对象来访问，但是静态数据成员并不属于某个对象。
- 在类外定义并初始化，默认情况下，基本类型的静态数据成员初始化为 0
- 生命周期与程序相同。
- 静态成员函数无 `this` 指针，只能访问静态成员。

```cpp
static int count = 0; //这个count静态数据成员可以用于计算全局中创建对象的数量。
```

## 静态成员函数 (Static Member Functions)与 `this` 指针

- 静态成员函数无 `this` 指针，因此只能访问静态成员。
- `this` 指针不是对象本⾝的⼀部分，即 `this` 指针占⽤的内存不会反映在对对象执⾏ `sizeof` 作的结果中，而是由编译器作为隐式参数传递给对象的每个⾮静态成员函数。但每个对象都可以通过 `this` 指针来访问⾃⼰的地址。
- `this` 指针的类型取决于对象的类型，以及使⽤ `this` 的成员函数是否声明为 `const`。例如，在 `Employee` 类的⾮ `const` 成员函数中，`this` 指针的类型为 `Employee* `。在 `const` 成员函数中，`this` 指针的类型为 `const Employee*` 。
```cpp
class Calculator {
public:
    static int add(int a, int b) { return a + b; }
};
```

可以使用 `this` 指针来实现**级联函数调用（Cascaded Function Calls）**，也就是**链式调用（Method Chaining）**，具体原因是，成员函数通过 `return *this;` 返回了相应类型的对象的引用，因此这个返回值可以接着作为一个该类型的对象继续调用。
`Tips:` 实现链式调用**必须返回引用**！否则返回一个对象（该对象的**新拷贝**）这不是我们想实现的。

```cpp
Time& Time::setHour(int hour){...
return *this}
Time& Time::setMinute(int minute){...
return *this}
Time& Time::setSecond(int second){...
return *this}

Time t;
t.setHour(16).setMinute(55).setSecond(59);
```
# 10. 运算符重载 (Operator Overloading)

## `String` 类的重载例子

- `substr (0,14)` ：从第一个字符开始向后截取14个字符；如果只有一个参数，则截取该索引位置及其之后的全部子字符串。如 `substr (5)` 则是截取第六个（索引为5）及其之后的字符串。
- `>=` `<=` `==` ：先根据字典（ASCII）判断，然后再判断字符串长度，短的 < 长的。
- `"apple" < "banana"` -> `true`；
- `"apple" < "applepie"` -> `true`；
- `"cat" < "Cat"` -> `false` ** (`c > C`)
- `"hello" <= "hello"` -> `true`
## 运算符重载

要在类对象上使⽤运算符，必须为该类定义重载运算符函数，但有三个例外：
- 赋值运算符 `=` 可用于将右值分配给左值。但是默认的赋值运算符对于具有指针成员的类是危险的，因此极度推荐显式地给出赋值运算符重载，这样才能实现**深拷贝**来避免默认状态中浅拷贝带来的各种风险，同时还要进行自赋值检查。如果需要支持链式调用，函数返回值则不需要加 `const` 关键字，反之，要加。

```cpp
MyClass& operator=(const MyClass& other) { 
	if (this == &other) {
		return *this; //自赋值检查
}
```

- 取址运算符 `&` 返回指向对象的指针;此运算符也可以重载；
- 逗号 `,` 逗号运算符先计算左侧的表达式，再计算右侧的表达式，并返回后⼀个表达式的值。

我们**不能重载**没有的运算符，但是可以重载**几乎所有**现有的运算符，除了：`.` `.*`（pointer to member） `::` `?:` 
重载无法修改运算符的：1、优先级、2、结合性（从左往右、从右往左）3、元数：左右元，一元、二元。
运算符**如何处理基本类型的值的含义**不能通过运算符重载来更改，例如：不能使 + 运算符减去两个整数，运算符重载仅适⽤于**⽤⼾定义类型的对象**，或者**⽤⼾定义类型的对象与基本类型的对象的混合**。

对对象进行操作时参数列表最好是对象的引用；
- 值传递：传入参数副本，不影响原对象，可能有拷贝开销。
- 引用传递：传入别名，可修改原对象，避免拷贝。
## 成员函数重载

- 左操作数为类对象，或者对类对象的引用。
- 二元运算符一个参数，一元无参数。

```cpp
class Complex {
public:
    double real, imag;
    Complex(double r=0, double i=0) : real(r), imag(i) {}
    Complex operator+(const Complex& o) const { return {real+o.real, imag+o.imag}; }
    Complex& operator+=(const Complex& o) { real+=o.real; imag+=o.imag; return *this; }
    Complex& operator++() { ++real; ++imag; return *this; }
    Complex operator++(int) { Complex t=*this; ++*this; return t; }
};
```

**下标访问**时应提供两个版本的重载函数：
```cpp
int& operator[](int num); // 可修改版本，返回的是相应数据的引用
int operator[](int num) const; // 只读版本，返回对应数据的拷贝，只读版本的函数必须要有const来作为区分两个版本的函数签名！
```
## 非成员函数重载 (友元)

- 当左操作数非本类对象时，如 `ostream << obj`。
**为什么要声明为友元函数而非成员函数？** 如果是成员函数，那么左元已经被确定为该对象（见上），故无法实现 `cout << object` 而只能实现 `object << cout` 来输出内容，这不符合我们的习惯，更不是我们想要的效果。对于输入操作符 `cin` 同样需要声明为友元函数。

```cpp
class Complex {
    friend ostream& operator<<(ostream& output, const Complex& c) {
        output<<...<<endl;
        return output; //返回ostream对象的引用是为了可以实现链式调用
    }
    friend istream& operator>>(istream& input, const Complex& c) {
	    input>>...>>endl;
	    return input;
    }
};
```

类的⼀元运算符可以重载为不带参数的⾮静态成员函数，也可以重载为具有⼀个参数的⾮成员函数，该参数必须是类的对象（或对对象的引⽤）如 `!` 。

**成员函数永远比非成员函数少一个参数（ `this` 指针指向的对象，做左值）**

## 前后缀运算符重载 `++` `--` 

前缀增量：
- 作为成员函数： `Date& operator++();`
- 作为友元函数： `Date& operator++( Date& )`
重载的前缀增量运算符返回对当前 `Date` 对象（即刚刚递增的对象）的引⽤。发⽣这种情况是因为当前对象 `*this `作为 `Date & `返回，允许将预递增的 `Date` 对象⽤作左值，这就是内置前缀递增运算符的工作方式。

后缀增量：
- 作为成员函数： `Date operator++( int )` 
- 作为友元函数： `Date operator++( Date& , int )`
后缀增量的函数签名 `int` 作为一个虚拟值来告诉编译器应该执行哪种增量加法。
为了模拟内置后缀递增的效果，我们必须返回 `Date` 对象的未递增副本 `temp` ，然后通过实用函数 `helpIncrement` 来对对象 `*this` 实现递增。
**为什么不能返回引用而要返回值？** 因为当声明局部变量的函数退出时，局部变量 `temp` 会被销毁，此时引用指向的真实数据就已经不存在了。

## 动态内存管理（Dynamic Memory Management）

- 为对象分配内存： `Date* dateptr = new Date();` `new` 会为创建的对象分配合适的内存同时调用构造函数并且返回这个对象的内存地址。
- 释放内存： `delete dateptr;` 销毁对象被分配到的内存地址，如果内存使用完不进行释放就会造成**内存泄漏**，这就是为什么要在析构函数中销毁内存，尽可能保证内存不泄露。
（注意：当内存被销毁后**不要二次销毁**，否则会出现错误。推荐的做法是销毁后立刻设为 `nullptr` ， `nullptr` 不受 `delete` 影响）

- 通过指针声明数组：
```cpp
int* ptr; // 正确！这个指针类型为int，可以通过指针指向一个数据为int的数组
int* ptr[]; // 错误!声明了一个包含int*指针的数组 而不是包含int的。
```

- 为数组分配内存： `int* gradesArray = new int[ 10 ]{};` 此处显⽰的空⼤括号集表⽰应为每个元素使⽤默认初始化，对于基本类型，每个元素都设置为 0。 `ptr ( new int [size])` 
- 销毁数组指针内存： `delete[] ptr;` 
## 类型转换和 `explicit` 关键字

当我希望对象被转换为 `char*` 类型的数据时，需要为这个类定义一个转换操作符。将这个转换操作符声明为 `MyClass::operator char *() const;` 可以注意到**没有显式的返回类型**，这是因为返回类型已经由操作符的名称（`char *`）隐含指定了。

当然也可以显式地调用 `static_cast<char *>(s)` ，编译器将生成 `s.operator char *()` 。

对于C++中的单参数构造函数就会出现编译器对于这类未知的类型会进行隐式的类型转换（有些时候不是我们希望的），所以需要用到 `explicit` 关键字来告诉编译器我们不想进行隐式转换。
**`explicit`  关键字用于修饰单参数构造函数，阻止隐式类型转换。** 

```cpp
class MyInt {
public:
    explicit MyInt(int x) : value(x) {}
    int value;
};

void printInt(const MyInt& mi) {
    std::cout << mi.value << std::endl;
}

int main() {
    printInt(42); // 错误：因为有 explicit ,不能从 int 隐式转换为 MyInt
}
```

# 11-12. 继承与多态（Inheritance and Polymorphism）

## 继承（Inheritance）

在基类没有默认构造函数的时候，派生类必须通过显式地调用基类的构造函数来初始化。如果基类存在可访问的默认构造函数，那么派生类可以在初始化时不写基类构造函数。（但是为了可读性，还是非常建议书写）

```cpp
BasePlusCommissionEmployee::BasePlusCommissionEmployee(
    const string &first, const string &last, const string &ssn,
    double sales, double rate, double salary )
    : CommissionEmployee( first, last, ssn, sales, rate )  // 显式调用基类构造函数
{
    setBaseSalary( salary ); // 设置底薪
}

```

要注意：派生类对象**无法访问**基类的私有数据成员，因此如果基类数据成员要可以被继承，应当设置为 `protected` ；当然也可以通过基类 `getsth()` 成员函数来访问。（继承受保护数据成员会略微提⾼性能，因为我们可以直接访问数据成员，⽽不会产⽣调⽤ `set` 或 `get` 成员函数的开销）

但是，对于基类中的受保护数据成员，如果基类实现发⽣更改，我们可能需要修改该基类的所有派⽣类。（最好还是使用 `private` 来保护数据成员，并通过接口来让派生类访问基类数据）。如果需要在派生类访问基类成员函数，只需在函数名前加上 `className::` 即可

`Tips:` 基类构造函数、析构函数和重载赋值运算符（第 10 章）**不能被派⽣类继承** ，但是可以调用基类的重载版本。在 `C++11` 中也可以可以通过 `using BaseClass::BaseClass;` 来“继承”基类构造函数。

如果一个派生类**仅仅**是“继承”了基类的构造函数，而没有自己明确定义任何构造函数，编译器依然会为这个派生类生成一个默认构造函数 。基类构造函数的默认参数不会被直接继承 。取而代之的是，编译器会在派生类中生成一组 **重载的（overloaded）** 构造函数来模拟默认参数的效果 。

例如：如果基类有 `Base(int a, bool b = true)`，它不会在派生类中变成 `Derived(int a, bool b = true)`。而是会生成两个独立的构造函数：
- `Derived(int a, bool b)` 
- `Derived(int a)` 

继承 `public` `protected` `private` 图谱：


## 多态（Polymorphism）

**多态实现必须满足的条件是：**
- 基类有虚函数
- 通过基类指针（或者引用）进行调用
如果没有虚函数，即使指针 `ptr` 实际指向一个 `Derived` 对象，但由于 `identify()` 不是虚函数，且 `ptr` 的类型是 `Base*` ，所以调用的是 `Base::identify()`。

```cpp
class Base {
public:
    void identify() {...}
     ~Base() {} 
};

class Derived : public Base {
public:
    void identify() {...}
};

int main() {
    Base* ptr = new Derived(); 
    ptr->identify(); //调用的是Base的identify函数，因为静态绑定
    
    delete ptr;
    return 0;
}
```

但如果基类存在 `virtual` 虚函数，调用 `ptr->identify()` 会在运行时检查到 `ptr` 指向的是一个 `Derived` 对象，因此会执行 `Derived::identify()`。

```cpp
class Base {
public:
    virtual void identify() {...}
    virtual ~Base() {} 
};

class Derived : public Base {
public:
    void identify() override {...}
};

int main() {
    Base* ptr = new Derived(); // 指针是 Base 类型，但指向 Derived 对象  
    // 因为 identify() 是虚函数，所以调用哪个版本在运行时由 ptr 指向的实际对象类型 (Derived) 决定。
    ptr->identify();
    delete ptr;
    return 0;
}
```

`Tips:` 基类析构函数在派⽣类析构函数之后⾃动执⾏。
可以将成员函数和类声明为 `final` 从而确定最后一版的代码是什么样的。
```cpp
virtual someFunction( parameters ) final;
class MyClass final  // 这个类不能再成为基类
{
// class body
};
```

通过**容器（vector）** 来实现多态：

```cpp
// create vector of three base-class pointers
vector< Employee * > employees( 3 );

// initialize vector with pointers to Employees
employees[ 0 ] = &salariedEmployee;
employees[ 1 ] = &commissionEmployee;
employees[ 2 ] = &basePlusCommissionEmployee;
```
### 抽象类（通常作为基类使用）

一个类之所以成为抽象类，是因为它声明了**一个或多个纯虚函数 (pure virtual functions)** 。
抽象类不能直接用来实例化对象，纯虚函数通常不提供实现代码，尽管C++允许这样做，但派生类**仍然得重写纯虚函数**，否则该派生类也将成为**抽象类**。
如果派生类要继承自这个抽象基类，就必须 `override` 其中的所有的**纯虚函数**。

创建一个纯虚函数： `virtual void draw() const = 0;` `= 0` 是一个说明符。

虽然不能创建抽象类的对象，但我们可以声明**指向抽象类的指针或引用** 。这些指针和引用可以指向任何继承自该抽象类的**具体派生类的对象** 。

### 动态转换

`dynamic_cast` 主要用于执行所谓的“**向下转型 (downcasting)**” ，也就是将一个基类指针（或引用）转换为其派生类的指针（或引用），这样做的目的是为了**能够调用派生类独有的、未在基类中定义的成员函数 。** 如果：
- 转换成功：那么 `dynamic_cast` 会返回一个指向该对象的、类型为“目标类型”的有效指针 。
- 转换失败：如果源指针所指向的对象的实际类型**不是**目标类型或其子类，转换会失败， `dynamic_cast` 将返回一个**空指针 `nullptr`** 。
因此转换的结果可以作为判断的条件，因为 `nullptr` 可以被隐式转换为布尔类型数值用于判断。

`dynamic_cast` 会在运行时检查对象的底层类型（是否是目标类型或者子类），而 `static_cast` 不会 。

```cpp
if (Dog* dogPtr = dynamic_cast<Dog*>(animalPtr)){
// 执行该派生类特有的成员函数；
}
```

`typeid` 运算符处于`type_info` 类，用于存储关于特定类型的具体信息 。不能直接创建`type_info` 的对象，只能通过 `typeid` 运算符来获取。

`type_info` 类最重要的成员函数之一是 `name()`，这个函数返回一个C风格的字符串（`const char*`），其中包含了类型的名称 。例如，对于`BasePlusCommissionEmployee` 类的对象，`name()` 可能会返回 `"class BasePlusCommissionEmployee"` 。但是`name()` 函数返回的字符串的具体格式**可能因编译器而异** 。
更建议使用：`typeid(*ptr) == typeid(Derived)` 这种方式比较 `name()` 返回的字符串，不受编译器限制。

# 13. 输入输出处理

### `Typedef` 

`typedef` 是C++中的一个关键字，用于为已有的数据类型创建一个新的名字（别名），但并不会创建一个新的数据类型。`iostream` 库提供了许多 `typedef`，作为类模板特化版本的别名，以方便使用 。

`std::basic_ifstream<char, std::char_traits<char>>` 这个名字太长，不方便日常使用。因此，C++标准库定义了一个别名：
`typedef std::basic_ifstream<char,std::char_traits<char>> ifstream;` 这样就可以直接使用简洁的 `ifstream`，而它背后代表的就是那个完整的、专用于 `char` 类型的类。

- `ifstream` 是 `basic_ifstream` 针对 `char` 类型的专用化版本 。
- `ofstream` 是 `basic_ofstream` 针对 `char` 类型的专用化版本 。
- `fstream` 是 `basic_fstream` 针对 `char` 类型的专用化版本 。
`typedef` 的主要目的是**增强代码的可读性**和**简化复杂的类型声明**。

### Formatted I/O (格式化 I/O)

- 格式化I/O是高层次的输入输出方式，它将字节序列解析为或组织成有意义的数据类型。
- C++的I/O是**类型安全**的 ，I/O操作会对数据类型进行检查 。如果数据类型不匹配，编译器会报错或在运行时设置流的错误状态位 。
例如：当你使用 `cout << 123;` 时，流中写入的是字符 `'1'`, `'2'`, `'3'`，而不是整数123在内存中的4字节二进制表示。这使得输出结果是人类可读的，并且通常具有很好的平台可移植性。

### Unformatted I/O (非格式化 I/O)

非格式化I/O是低层次的输入输出方式，它直接处理原始的字节流，不关心这些字节代表何种数据类型。
- 它直接操作原始字节（raw bytes），将指定数量的字节在设备和内存之间进行传输 。在这种传输中，单个字节是其关注点 。
- 主要通过`istream`的`read()`和`ostream`的`write()`成员函数来执行 。`read()`将字节读入字符数组 ，`write()`将字符数组中的字节写出 。

### 输出流操作

- 直接输出`char *` 变量会打印其指向的C风格字符串；若要输出其内存地址，需要将其转换位`void *` 类型 （通用指针，可以指向任何数据类型的内存地址，但**不能解引用**，从 `int *` 类型转换而来的 `void *` 只能再转换回 `int *` ）
```cpp
int main()
{
    const char *const word = "again";

    cout << "Value of word is: " << word << endl
         << "Value of static_cast< const void * >( word ) is: "
         << static_cast< const void * >( word ) << endl;
} // end main

// 输出结果：
// Value of word is: again
// Value of static_cast< const void * >( word ) is: 0135CC70
```
- `ostream`的成员函数 `put()` 用于输出单个字符 。
```cpp
cout.put( 'A' ).put( '\n ' ); // 正常输出字符内容
cout.put( 65 ) // 输出'A';
```

在设置了多种输出格式后，如果想恢复到之前的状态，最可靠和便捷的方法是使用`flags()` 成员函数 。
- **保存当前格式状态**：在更改格式之前，调用不带参数的 `flags()` 函数。它会返回一个 `ios_base::fmtflags` 类型的值，这个值代表了当前流的所有格式设置。你需要将这个值保存在一个变量中 。 `ios_base::fmtflags originalFormat = cout.flags();`
- **恢复格式状态**：在完成了需要特殊格式的输出之后，调用带参数的 `flags()` 函数，并将第一步中保存的那个变量传递给它。这样就可以将流的格式状态瞬间恢复到之前保存的状态 。`cout.flags( originalFormat );`

`cerr` (无缓冲标准错误流)：输出都会被**立即显示**，而不会在缓冲区中等待 。
`clog` (有缓冲标准错误流)：输出内容会先存放在缓冲区中，直到缓冲区满了或者被显式刷新（flush）时才会显示出来 。

`setw`只生效一次，其他都是永久生效。
### 输入流操作

`EOF` 是一个在遇到文件末尾时返回的整数值 ，它是一个预定义的、系统相关的值，通常为-1。
`EOF` 的值可能无法被 `char` 类型表示，所以在接收可能返回 `EOF` 的函数（如 `cin.get()`）的返回值时，应该使用 `int` 类型的变量来存储，以确保能正确地与 `EOF` 进行比较 。

`cin.eof()` 是 `istream` 类的一个成员函数，用于检查流是否到达了文件末尾。在流的 `eofbit` 状态位被设置时返回 `true`，否则返回 `false`。
**关键触发时机**：`eof()` 函数**仅在程序试图读取并越过流的最后一个字符之后**，才会返回 `true` 。换言之，仅仅读取到最后一个字符，但没有尝试再往下读时，`eof()` 仍然会返回 `false`。

一个非常常见的错误是使用 `while(!cin.eof())` 来控制输入循环：假设流中只剩下最后一个数据。循环开始前，`cin.eof()` 是 `false`，循环条件成立。`cin >> my_variable;` 成功读取了最后一个数据。此时，流的指针在最后一个数据之后，但由于还没有**尝试越过它**，`eof()` 仍然是 `false`！循环会再次进入，但下一次 `cin >> my_variable;` 将会因为无数据可读而失败。结果是，循环体在最后一次成功读取后，又多执行了一次，导致对无效数据进行处理。

正确的做法是**将输入操作本身作为循环条件**。
```cpp
// 正确方式 1: 读取单词
while (cin >> my_variable) {
}
// 正确方式 2: 读取字符直到EOF
int character;
while ((character = cin.get()) != EOF) {
}
```

当用户输入错误的数据时，例如需要输入整数 `int` 但是输入了 `'A'` ，输入就会被设置为 `failbit` ，此时需要 `cin.ignore()` 来去除输入缓冲区的错误输入（不去除则一直停留），然后设置为 `cin.clear()` 来重置流状态，继续输入。 

还有一种方法就是在进入 `while(!cin.oef())` 之前先进行一次读取操作，然后在 `while` 中最后再读取下一条数据，这样的实际效果就是在尝试读取后再进行判断是否要进行处理，也就是倒数第二个数据处理完后立刻读取最后一条数据，然后再判断；只要对于同一条记录保证读取在判断之前即可。
```cpp
inClientFile>>account>>name>>balance;
while(!cin.eof()){
...
inClientFile>>account>>name>>balance;
}
```

### 其他输入操作

使用 `char` 类型的数组来表示字符串时（常见于随机文件读写，因为要规定每个数据段的大小）

```cpp
int main() { 
int id; 
char description[50];
std::cout << "请输入ID: "; 
std::cin >> id;  
std::cout << "请输入描述: "; std::cin.getline(description, 50); // 实际只会读取49个字符，还有一个位置留给'\0'
std::cout << "ID: " << id << "\n描述: " << description << std::endl; 
return 0; 
}
```

`cin.getline(buffer, size)` 函数是安全的。它会自动抛弃之前用户输入时留下的 `\n` ，最多只会读取 `size - 1` 个字符，（**但不能自动截取**！）然后自动在末尾添加 `\0`。在混合使用 `cin >>` 和 `cin.getline` 时，要用 `cin.ignore()` 来清理缓冲区。

还可以通过 `width` 来控制输入宽度：
```cpp
char userInput[20]; 
std::cout << "请输入一个单词 (最多19个字符): "; // 设置下一次cin操作的最大宽度为20 
std::cin.width(20);
```
### 流的状态位（Stream State Bit）

流主要有四种状态，由四个状态位来表示：`eofbit`、`failbit`、`badbit` 和 `goodbit` 。

`failbit` 是一个用于表示**可恢复的格式错误**的状态位。
- 当流操作遇到格式错误，且没有字符被成功读入时，`failbit` 就会被设置 。最典型的例子是，当程序期望输入一个数字时（`cin >> my_integer`），用户却输入了字母（如 "`hello`"）。
- `failbit` 被设置，流就进入了“失败”状态。后续对该流的所有I/O操作都会立即失效，直到这个错误状态被清除 。重要的是，导致格式错误的那些字符**并不会从输入流中丢失** 。它们仍然留在流中，等待程序去处理。
- **可恢复性**：`failbit` 错误通常被认为是**可恢复的** 。程序可以检测到这个错误，清除流的状态，忽略掉错误的输入，然后提示用户重新输入。

`badbit` 是一个用于表示**严重的、导致数据丢失的错误**的状态位。
- 当发生导致数据丢失的严重I/O错误时，`badbit` 就会被设置 。这通常是底层I/O系统出现了问题，而不是简单的格式错误。
- `badbit` 错误通常被认为是**不可恢复的** 。当发生这种错误时，程序通常无法继续正常执行I/O操作。
`failbit` 程序还能进行，只是要丢弃输入流中的错误。 `badbit` 会终止程序。

# 14. 文件读写处理（File Process）

要在 C++ 中执⾏⽂件处理，必须 `#include <fstream>` 以及 `<iostream>` ，这些头文件包含了为 `char I/O` 预定义的专用模板。 `fstream` 库为这些模板提供了 `typedef` 别名 `ifstream` `ofstream` 来支持 `char` 在文件中的输入输出。

## 序列化文件（Sequential File）

序列化文件一般通过流操作符 `<<` `>>` 来操作，因为其中的内容是格式化的，C++已经组织好了结构，更易读但是不够灵活。

- 打开文件时，需要通过创建 `ofstream` 对象，并将这个文件操作对象与文件相关联：

```cpp
oftream outClientFile("clients.txt",ios::out);
// clients.txt为文件名，ios::out为打开方式"，要注意ios::out会默认清空当前文件中的全部内容！
ofstream outClientFile; // 也可以先创建，再关联
outFileClientFile.open("clients.txt",ios::out);
```

在尝试打开文件后，**必须进行检查以确保操作成功**，可以用 `if (!outClientFile)` 来进行判断 。这里利用了对`!` 操作符的重载，如果文件打开失败（例如，文件不存在且无法创建，或者没有写入权限），这个表达式的结果为 `true` 。
-重载 `void *` 运算符也是一样的效果，只是判断条件变成是否 `nullptr` （`true / false`）-


如果打开失败，程序通常会输出错误信息并使用`exit(EXIT_FAILURE)` 终止运行 。如果传递给 `exit()` 的参数是 `EXIT_SUCCESS` 则表明程序正常退出，传递其他值则说明⽰程序因错误⽽终⽌。

`if (!outClientFile)` 检查的就是 `failbit` 或 `badbit` 是否被设置。让用户输入信息时的：`while (inClientFile >> account >> name >> balance)` 循环的持续条件也是基于这些状态位。

- 关闭文件：当`main` 函数结束时，`ofstream` 对象 `outClientFile` 的**析构函数**会被自动调用，这个析构函数会负责关闭文件 。也可以通过调用`close()` 成员函数来显式地关闭文件 。
强烈建议：一旦文件不再需要，就应立即关闭它 。

文件数据查找：
- **`seekg`**：“seek get”，用于**输入流**（`istream`及其派生类，如 `ifstream`），它移动的是“获取指针”（get pointer），这个指针决定了下一次**读取**数据的位置 。
- **`seekp`**：“seek put”，用于**输出流**（`ostream`及其派生类，如 `ofstream`），它移动的是“放置指针”（put pointer），这个指针决定了下一次**写入**数据的位置 。

## 随机文件访问（Random Access File）

随机文件读取要求⽂件中的所有记录具有相同的固定⻓度，这样就可以很容易地快速计算任何记录字段相对于⽂件开头的确切位置（字节数）。这是一种更加原始的方式，直接通过对字节进行读取写入操作，而且更加灵活。
- **`ostream::write()`**: 这个函数用于**非格式化**输出。它从指定的内存地址开始，将固定数量的字节原封不动地写入文件 。
- **`istream::read()`**: 用于非格式化输入。它从文件中读取固定数量的字节，并将其存入指定的内存地址 。
为了实现对内存中字节的操作，必须将不同类型的指针转化为可操作的 `const char *` ，因此要将其强制转化为字节形式；

```cpp
// 一定要通过二进制打开文件
ofstream outCredit("credits.dat",ios::out|ios::binary);
// 当然也可以一步到位
fstream inoutCredit("credits.dat",ios::in|ios::out|ios::binary);

reinterpret_cast<const char *>(&blankClient) // 强制类型转换
outCredit.write(reinterpret_cast<const char *>(&client),sizeof(ClientData));
// 在指定位置写入sizeof(ClientData)字节量的数据
```
`reinterpret_cast` 在编译时执⾏，并且不会更改其作数指向的对象的值。

那么应该如何将数据存储在⽂件中的确切位置？对于写入操作：
```cpp

// 通过seekp来确定写入操作的内存位置，recordNumber是记录编号，写入位置的计算方法如代码所示
outCredit.seekp((recordNumber-1) * sizeof(ClientData));
// 确定位置然后进行写入操作
outCredit.write(reinterpret_cast<const char *>(&client),sizeof(ClientData));
```

# 其他内容

## 模板 `Template` 和泛型编程

使用一个**模板T**来代表所有可能需要操作的数据类型，然后对这个模板T进行操作，后面需要实例化的时候再添加具体数据类型。例如声明了一个类 `Stack` 通过 `deque` 类中的 `stack` 栈库 来进行操作。
```cpp
#include<deque>
template< typename T >
class Stack
{
public:
    // return the top element of the Stack
    T& top()
    {
        return stack.front();
    } // end function template top

    // push an element onto the Stack
    void push( const T &pushValue )
    {
        stack.push_front( pushValue );
    } // end function template push

    // pop an element from the stack
    void pop()
    {
        stack.pop_front();
    } // end function template pop

    // determine whether Stack is empty
    bool isEmpty() const
    {
        return stack.empty();
    } // end function template isEmpty

    // return size of Stack
    size_t size() const
    {
        return stack.size();
    } // end function template size

private:
    std::deque< T > stack; // internal representation of the Stack
}; // end class template Stack
```

当需要用于具体数据类型时，直接声明：
```cpp
	Stack<double> doubleStack;
	Stack<int> intStack;
```

C++标准数组类 `array` 模板声明：
```cpp
template< class T, size_t n > // class和typename在模板声明中可以互换
// 实例化
array<double, 100> arr1; // 包含 100 个元素的 doubles 类模板特化数组arr1
```

`stack` 容器适配器类模板的声明类似于：`template <class T, class Container = deque<T>>`
- 这里的第二个参数 `Container` 有一个默认值 `deque<T>`。
- 它位于参数列表的末尾，遵循了“**默认参数必须靠右**”的规则。
- 因此，当你声明`stack<int>` 时，编译器会自动使用默认的 `deque<int>` 作为底层容器 。
- 如果你想使用不同的容器，比如`vector`，你就需要显式提供第二个参数：`stack<int, vector<int>>` 。

## 模板函数重载（Template Overloaded）

1、使用其他函数模板重载：

```cpp
#include <iostream>

// 模板 1: 接受一个参数
template<typename T>
void print(T value) {
    std::cout << "Template 1: " << value << std::endl;
}

// 模板 2: 接受两个参数 (重载版本)
template<typename T1, typename T2>
void print(T1 val1, T2 val2) {
    std::cout << "Template 2: " << val1 << " and " << val2 << std::endl;
}

int main() {
    print(10);             // 调用模板 1
    print("Hello", 20.5);  // 调用模板 2
}
```

2、使用非模板函数进行重载：

```cpp
#include <iostream>
#include <cstring> // for strcmp

// 函数模板
template<typename T>
T max(T a, T b) {
    std::cout << "Calling template version of max" << std::endl;
    return a > b ? a : b;
}

// 非模板函数 (重载版本)
// 为 const char* 类型提供一个特化的实现
const char* max(const char* a, const char* b) {
    std::cout << "Calling non-template version for const char*" << std::endl;
    return strcmp(a, b) > 0 ? a : b;
}

int main() {
    // 调用函数模板，因为参数是int，与非模板函数不匹配
    std::cout << "Max of 3 and 5 is " << max(3, 5) << std::endl;
    std::cout << "--------------------" << std::endl;
    
    // 调用非模板函数，因为参数是const char*，精确匹配
    const char* s1 = "hello";
    const char* s2 = "world";
    std::cout << "Max of s1 and s2 is " << max(s1, s2) << std::endl;
}
```

只要能让编译器匹配到唯一一个函数或者模板函数即可。

## `const_cast`

`const_cast` 是一个类型转换操作符，它允许你**移除或添加**一个变量的 `const` 或 `volatile` 限定符 。主要用于临时“去掉”一个变量的 `const` 属性，以便可以对其进行修改 。

```cpp
const char* maximum(const char *first, const char *second){}
// 将maximum函数返回值const转换为非const char* maxPtr
char *maxPtr = const_cast<char *>(maximum(s1, s2));
```

## `mutable` 类成员

`mutable` 是一个存储类说明符，它提供了一种**在类设计层面**绕过 `const` 限制的方法 。
当一个类的**数据成员**被声明为 `mutable` 时，即使这个类的对象是 `const` 的，或者在类的 `const` 成员函数中，这个 `mutable` 成员也**永远是可修改的** 。
可以这么说：`mutable` 就是为了让 `const` 成员函数修改而生的！

## 命名空间（Namespace）

- **未命名命名空间 (Unnamed Namespaces)**
```cpp
#include <iostream>
using namespace std;

int integer1 = 98; // global variable

// create namespace Example
namespace Example
{
   // declare two constants and one variable
   const double PI = 3.14159;
   const double E = 2.71828;
   int integer1 = 8;
   void printValues(); // prototype

   // nested namespace
   namespace Inner
   {
      // define enumeration
      enum Years { FISCAL1 = 1990, FISCAL2, FISCAL3 };
   } // end Inner namespace
} // end Example namespace

// create unnamed namespace
namespace
{
   double doubleInUnnamed = 88.22; // declare variable
} // end unnamed namespace

int main()
{
   // output value doubleInUnnamed of unnamed namespace
   cout << "doubleInUnnamed = " << doubleInUnnamed;

   // output global variable
   cout << "\n(global) integer1 = " << integer1;

   // output values of Example namespace
   cout << "\nPI = " << Example::PI << "\nE = " << Example::E
      << "\ninteger1 = " << Example::integer1 << "\nFISCAL3 = "
      << Example::Inner::FISCAL3 << endl;

   Example::printValues(); // invoke printValues function
} // end main

// display variable and constant values
void Example::printValues()
{
   cout << "\nIn printValues:\ninteger1 = " << integer1 << "\nPI = "
      << PI << "\nE = " << E << "\ndoubleInUnnamed = "
      << doubleInUnnamed << "\n(global) integer1 = " << ::integer1
      << "\nFISCAL3 = " << Inner::FISCAL3 << endl;
} // end printValues
```
未命名命名空间有一个隐式的 `using` 指令，所以它的成员可以被直接访问，看起来就像在全局作用域中一样，无需任何限定符 。

要访问嵌套命名空间中的成员，你需要使用多个作用域解析运算符，例如`Example::Inner::FISCAL3`

在`Example` 命名空间的函数 `printValues` 内部，直接使用 `integer1` 会访问到属于 `Example` 的版本 。如果你想在这个函数内部访问全局的`integer1`，则必须在它前面加上全局作用域解析符 `::`，即 `::integer1` 。

`Unnamed` 命名空间的优先级高于全局命名空间，如果要使用全局命名空间需要和前一样的操作。

`WARNING:` **绝对不要在头文件中使用 `using` 指令** ！

## 多重继承（Multiple Inheritance）

多重继承允许一个派生类同时从**两个或更多的基类**中继承成员 。

```cpp
class Derived : public Base1, public Base2
{};
```

构造函数的调用：基类构造函数的**调用顺序**由派生类定义时的**继承顺序**决定，而不是由它们在成员初始化列表中出现的顺序决定 。

```cpp
// 派生类的构造函数定义
Derived::Derived(int val1, char val2, double val3)
    : Base1(val1), Base2(val2), real(val3) // 调用基类构造函数
{
}
```

### “菱形继承”歧义 (Diamond Inheritance)

当一个类D同时继承自B和C，而B和C又都继承自同一个基类A时，就会形成一个菱形的继承结构。
- **问题所在**: 默认情况下，D中会包含**两份**A的成员（一份通过B继承，一份通过C继承） 。当你尝试在D中访问A的成员时，编译器不知道该用哪一份，从而产生歧义 。

为了解决这个问题，我们需要使用**虚继承（Virtual Inheritance）**，虚继承可以通过**虚基类（Virtual Base Class）** 来实现。

当一个基类被声明为 `virtual` 继承时，所有从它派生的子类将共享这个基类的**唯一一个实例**，在这种情况下，最终的派生类（菱形的底部）只会包含一份最顶层基类的子对象，从而消除了歧义。

```cpp
class DerivedOne : virtual public Base { ... };
class DerivedTwo : virtual public Base { ... };
class Multiple : public DerivedOne , public DerivedTwo { ... };
```












