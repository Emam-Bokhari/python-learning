# Method	কাজ
# append()	শেষে একটি item যোগ করে
# insert()	নির্দিষ্ট index-এ item যোগ করে
# remove()	নির্দিষ্ট value মুছে দেয়
# pop()	item মুছে দিয়ে সেই value return করে
# len()	item-এর সংখ্যা জানায়
# sort()	list সাজায়

food_list=["apple","mango","banana","strawberry"]

food_list.append("jackfruit")

food_list.remove("mango")

food_list.insert(0,"orange")

print(len(food_list))

# reverse
print(food_list.sort(reverse=True))
