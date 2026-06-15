#START
#   WHILE true
#       SET error_list = []
#       INPUT "password".lower
#       IF "password" is in password THEN
#           ADD "password is too weak" TO error_list
#           PRINT("ACCESS DENIED")
#       END IF
#       IF LENGTH(password) < 8 THEN
#           ADD "password is too shot" TO error_list
#            PRINT("ACCESS DENIED")
#       END IF
#       IF error_list IS EMPTY THEN
#           PRINT "ACCESS GRANTED"
#           BREAK
#       ELSE
#           PRINT "error_list"
#       END IF
#   END WHILE
#STOP

atempts = 0
while True:
    atempts = atempts + 1
    error_list =[]
    password = input("enter your password: ").lower()
    if "password" in password:
        error_list.append("your password is too weak")
        print("ACCESS DENIED")
    if len(password) < 8:
        error_list.append("your password is too short")
        print("ACCESS DENIED")

    if error_list == []:
        print("ACCESS GRANTED")
        break
    elif atempts == 3:
        print(error_list)
        break