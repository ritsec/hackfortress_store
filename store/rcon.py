import valve.rcon
import sys
from random import randint,choice
from threading import Thread
from time import sleep

SERVER_ADDRESS = ("127.0.0.1", 27015)
PASSWORD = "1337pwnage"

REDTEAM = ['hulto', 'cictrone']
BLUTEAM = ['drummergeek', 'clev']

THREADS = []

#Todo make sure that you don't accidently apply the same affect to the same person multiple times. Spread the pain

def rcon_exec(cmd, addr=None, passwd=None):
    if(addr == None):
        addr = SERVER_ADDRESS
    if(passwd == None):
        passwd = PASSWORD
    return valve.rcon.execute(addr, passwd, cmd)

def restore_countdown(cmd, seconds):
    sleep(seconds)
    rcon_exec(cmd)

def apply_effect(ef, team):
    target = ""
    if("slap" in ef or "6" in ef):
        if(team == BLUTEAM):
            target = "@blu"
        elif(team == REDTEAM):
            target = "@red"
        else:
            target = "@dead"
    elif("1_" in ef):
        target = choice(team)


    if(ef == "light_slap"):
        rcon_exec("sm_slap %s %d" % (target, randint(10,30)))
        print("light slap")
    elif(ef == "medium_slap"):
        rcon_exec("sm_slap %s %d" % (target, randint(30,40)))
        print("med slap")
    elif(ef == "heavy_slap"):
        rcon_exec("sm_slap %s %d" % (target, randint(50,60)))
        print("Heavy slap")
    
    elif(ef == "1_10_blind"):
        blind_cmd = "sm_blind %s " % (target)
        rcon_exec(blind_cmd + "255")
        t = Thread(target = restore_countdown, args = (blind_cmd + "0", 10))
        t.start()
        THREADS.append(t)
        print(blind_cmd + " 255")
    elif(ef == "1_20_blind"):
        blind_cmd = "sm_blind %s " % (target)
        rcon_exec(blind_cmd + "255")
        t = Thread(target = restore_countdown, args = (blind_cmd + "0", 20))
        t.start()
        THREADS.append(t)
        print("1/20 blind")
    elif(ef == "6_10_blind"):
        blind_cmd = "sm_blind %s " % (target)
        print(blind_cmd + "255")
        rcon_exec(blind_cmd + "255")
        t = Thread(target = restore_countdown, args = (blind_cmd + "0", 10))
        t.start()
        THREADS.append(t)
        print("6/10 blind")
    elif(ef == "6_20_blind"):
        blind_cmd = "sm_blind %s " % (target)
        rcon_exec(blind_cmd + "255")
        t = Thread(target = restore_countdown, args = (blind_cmd + "0", 20))
        t.start()
        THREADS.append(t)
        print("6/20 blind")

    elif(ef == "crits_6_15"):
        print("crits 15")
    elif(ef == "crits_6_30"):
        print("crits 30")

    elif(ef == "freeze_3"):
        # Get random 3
        targets = []
        tmp_team = team
        while(len(targets) < 3 and len(targets) <= len(team)):
            person = choice(tmp_team)
            targets.append(person)
            tmp_team.remove(person)
        for i in targets:
            rcon_exec("sm_freeze %s %d" % (i, 20))
            print("Freezeing %s" % i)

    elif(ef == "freeze_6"):
        rcon_exec("sm_freeze %s %d" % (target, 20))
        print("freeze 6")

    elif(ef == "1_10_drunk"):
        drunk_cmd = "sm_drug %s " % (target)
        rcon_exec(drunk_cmd + "1")
        t = Thread(target = restore_countdown, args = (drunk_cmd + "0", 10))
        t.start()
        THREADS.append(t)

        print("1/10 drunk")
    elif(ef == "1_20_drunk"):
        drunk_cmd = "sm_drug %s " % (target)
        rcon_exec(drunk_cmd + "1")
        t = Thread(target = restore_countdown, args = (drunk_cmd + "0", 20))
        t.start()
        THREADS.append(t)
        print("1/20 drunk")
    elif(ef == "6_10_drunk"):
        drunk_cmd = "sm_drug %s " % (target)
        rcon_exec(drunk_cmd + "1")
        t = Thread(target = restore_countdown, args = (drunk_cmd + "0", 10))
        t.start()
        THREADS.append(t)
        print("6/10 drunk")
    elif(ef == "6_20_drunk"):
        drunk_cmd = "sm_drug %s " % (target)
        rcon_exec(drunk_cmd + "1")
        t = Thread(target = restore_countdown, args = (drunk_cmd + "0", 20))
        t.start()
        THREADS.append(t)
        print("6/20 drunk")
    else:
        return -1
    
    #for i in THREADS:
    #    i.join()
    #return 0

if __name__ == "__main__":
    #res = rcon_exec(cmd=sys.argv[1])
    #print(res)
    apply_effect(sys.argv[1], REDTEAM)
