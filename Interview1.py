def funFunc(main):
    main_dict = {}
    for i in main:
        if i in main_dict:
            main_dict[i] += 1
        else:
            main_dict[i] = 1

    print(main_dict)
    values = list(main_dict.values())
    keys = list(main_dict.keys())
    print(keys)
    print(values)

funFunc("rudra")