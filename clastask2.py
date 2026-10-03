# try:
#         a = int(input())
#         b = int(input())
#         print(a/b)

# except ValueError:
#         print("Error!")


# except ZeroDivisionError:
#         print("Calculation finished")

# finally:
#         print("Calculation finished")









# Cities=['Dushanbe', 'Khujand', 'Bokhtar']
# try:
#     a = int (input())
#     print(Cities[a])
# except ValueError:
#     print("Its a letter stupid")
# except IndexError:
#     print("position does not exist")













# prices = {
#     "mouse": 100,
#     "keyboard":250,
#     "monitor":1200
# }



# try:
#     product = input()
#     num = int(input())
   
#     print("Total:", prices[product] * num)
# except KeyError:
#     print("Wrong key")
# except ValueError:
#     print("Wrong value")












# def calculate_average(values):
#     try:
#         l=[]
#         for i in values:
#             l.append(int(i))
#         print(sum(l)/len(l))
#     except ValueError as error:
#         print(error)
#     except ZeroDivisionError as error:
#         print(error)



# k = input().split()
# calculate_average(k)














# ??????????????????????
# def register_participant(name, age):
#     try :
#         a = str(name)
#         b = int (age)
#     except TypeError as error:
#             print(error)
#     except ValueError as error:
#          print(error)
        









# 6??








# 7??











# def price_per_item(total, quantity):
#        s=int(total)
#        a=int(quantity)
#        try:
#            return s / a
#        except ZeroDivisionError as error:
#            return(error)


# def build_report(order):
#         return price_per_item(order["total"], order["quantity"])
    
# def main():
#         order = {"total": 600, "quantity": 0}
#         print(build_report(order))


# main()













