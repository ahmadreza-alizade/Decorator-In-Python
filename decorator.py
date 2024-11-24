
def big_outer(t):
    def outer_show(func):
        def inner_show(name):
            f = func(name)
            text = t + name
            return(text)
        return(inner_show)
    return(outer_show)


@big_outer("Hello")
def show(name):
    return(name)

print(show(" ali"))

