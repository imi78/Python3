def loading_bar(percent):
    bar = []
    for i in range(10):  # make a list with "."
        bar.append('.')

    bars_to_fill = percent // 10  # calculates how many spaces should be filled

    for index in range(bars_to_fill):
        bar[index] = '%'  # substitutes the symbols in list at the given index

    if percent < 100:
        bar = f"{percent}% [{''.join(bar)}] \n Still loading..."
        return bar

    else:
        complete = f"100% Complete! \n [{''.join(bar)}]"
        return complete

    return bar


percent = int(input())
print(loading_bar(percent))