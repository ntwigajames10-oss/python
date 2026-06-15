#START
#   WHILE True
#       INPUT "secret_code"
#       IF secret_code == python123 THEN
#           PRINT "ACCESS GRANTED"
#           BREAK
#       ELSE
#           PRINT "ACCESS DENIED"
#       END IF
#   END WHILE
#STOP

while True:
    secret_code = input("secret_code: ").lower()
    if secret_code == "python123":
        print("ACCESS GRANTED")
        break
    else:
        print("ACCESS DENIED")