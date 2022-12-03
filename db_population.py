#!/user/bin/python3
'''
    This simple python script is used to populate the database with random data or similar. 
    It is not really random, but it is good enough for this purpose.
    The biggest problem is the differences between the database structure of each of us.
    I hope to solve this problem in the future.


    The usage of this script is to uncomment the functions you want to use and run it.
    Remeber to comment the functions you don't want to use.
    The functions are:
        populateUser(conn)
        populatePost(conn)
        populateLike(conn)
        populateComment(conn)
        populateBan(conn)
        populateFollow(conn)
    
'''
import sqlite3
from sqlite3 import Error
import random
import time as time
import json

# Insert the path to the database file here
db_file = '/tmp/wasa_TEST.db'

with open('tables_components.json', 'rb') as f:
    tables_components = json.load(f)
    f.close()

'''
Go to tables_components.json and add the attributes you use in each tables.
Each following dictionary is an example entries of a table, and each key is an attribute.
The followings functions are used to populate the database with random data, this obejct is used only to store the data.
'''
user = tables_components['user']
post = tables_components['post']
like = tables_components['like']
comment = tables_components['comment']
ban = tables_components['ban']
follow = tables_components['follow']

usernames_list = ['mina', 'seulgi', 'joy', 'haru', 'jhope', 'sooyoung', 'ballo', 'jennie', 'yoona', 'yeri', 'rose', 'tzuyu', 'sana', 'seohyun', 'hyoyeon', 'jin', 'jessica', 'tiffany', 'nayeon', 'momo', 'jihyo', 'jungkook', 'jimin', 'yuri', 'rm', 'wendy', 'sunny', 'irene', 'v', 'jeongyeon', 'dahyun', 'cha', 'suga', 'jisoo', 'lisa', 'chaeyoung', 'taeyeon', 'colla']

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

'''
    This function insert a new user in the database. 
    Each user had a unique ID and a username, other attributes are set to default. See populateUser() for more details.
'''
def addUser(conn):
    sql = ' INSERT INTO User(userID,username,userPropicURL,bio) VALUES (?,?,?,?) '
    cur = conn.cursor()
    cur.execute(sql, (user['userID'], user['username'],
                user['userPropicURL'], user['bio']))
    conn.commit()
    return cur.lastrowid

'''
    This function insert a new post in the database.
    Each post had a unique ID, a userID, other attributes are set to default. See populatePost() for more details.
'''
def addPost(conn):
    sql = ' INSERT INTO Post(postID,userID,postImageURL,caption) VALUES (?,?,?,?) '
    cur = conn.cursor()
    cur.execute(sql, (post['postID'], post['userID'],
                post['postImageURL'], post['caption']))
    conn.commit()
    return cur.lastrowid

'''
    This function insert a new like in the database.
    Each like had a  postID and userID. See populateLike() for more details.
'''
def addLike(conn):
    sql = ' INSERT INTO Like(postID,userID) VALUES (?,?) '
    cur = conn.cursor()
    cur.execute(sql, (like['postID'], like['userID']))
    conn.commit()
    return cur.lastrowid

'''
    This function insert a new comment in the database.
    Each comment had a uniqueID, a userID and postID. See populateComment() for more details.
'''
def addComment(conn):
    sql = ' INSERT INTO Comment(commentID, postID,userID,commentText) VALUES (?,?,?,?) '
    cur = conn.cursor()
    cur.execute(sql, (comment['commentID'], comment['postID'], comment['userID'],
                comment['commentText']))
    conn.commit()
    return cur.lastrowid

'''
    This function insert a new ban relationship in the database.
    Each ban relationship had a bannerID and bannedID. See populateBan() for more details.
'''
def addBan(conn):
    sql = ' INSERT INTO Ban(bannerID,bannedID) VALUES (?,?) '
    cur = conn.cursor()
    cur.execute(sql, (ban['bannerID'], ban['bannedID']))
    conn.commit()
    return cur.lastrowid

'''
    This function insert a new follow relationship in the database.
    Each follow relationship had a followerID and followedID. See populateFollow() for more details.
'''
def addFollow(conn):
    sql = ' INSERT INTO Follow(followerID,followedID) VALUES (?,?) '
    cur = conn.cursor()
    cur.execute(sql, (follow['followerID'], follow['followedID']))
    conn.commit()
    return cur.lastrowid

'''
    This function generate user with a incremental ID and a username from usernames_list. Other attributes are set to default.
'''
def populateUser(conn):
    for i in range(1, len(usernames_list)):
        user['userID'] = i
        user['username'] = usernames_list[i]
        addUser(conn)

'''
    This function generate a post with a incremental ID and a userID. Other attributes are set to default.
'''
def populatePost(conn):
    for i in range(1, len(usernames_list)):
        post['postID'] = i
        
        #It is not really random, but it is good enough for this purpose.
        if i % 2 == 0:
            post['userID'] = i
            addPost(conn)
        else:
            post['userID'] = i + 1
            addPost(conn)

'''
    This function generate a like with a random postID and userID.
'''
def populateLike(conn):
    random.seed(time.time())
    for i in range(1, len(usernames_list)):
        like['postID'] = random.randint(1, len(usernames_list))
        like['userID'] = random.randint(1, len(usernames_list))
        addLike(conn)

'''
    This function generate a comment with a random postID and userID. Other attributes are set to default.
'''
def populateComment(conn):
    random.seed(time.time())
    for i in range(1, len(usernames_list)):
        comment['postID'] = random.randint(1, len(usernames_list))
        comment['userID'] = random.randint(1, len(usernames_list))
        addComment(conn)

'''
    This function generate a ban relationship with a random bannerID and bannedID.
'''
def populateBan(conn):
    random.seed(time.time())
    for i in range(1, len(usernames_list)):
        ban['bannerID'] = random.randint(1, len(usernames_list))
        ban['bannedID'] = random.randint(1, len(usernames_list))
        if follow['bannerID'] != follow['bannedID']:    
            addBan(conn)

'''
    This function generate a follow relationship with a random followerID and followedID.
'''
def populateFollow(conn):
    random.seed(time.time())
    for i in range(1, len(usernames_list)):
        follow['followerID'] = random.randint(1, len(usernames_list))
        follow['followedID'] = random.randint(1, len(usernames_list))
        if follow['followerID'] != follow['followedID']:
            addFollow(conn)

    
def main():
    tables_names = ['User', 'Post', 'Follow', 'Like', 'Comment', 'Ban']
    conn = create_connection(db_file)
    with conn:
        #populateUser(conn)
        #populatePost(conn)
        #populateLike(conn)
        #populateComment(conn)
        #populateBan(conn)
        #populateFollow(conn)
        #clear_table(conn, tables_names[0])
        #print_table(conn, tables_names[0])
        pass
    return 0

'''
    This function clear a table in the database.
'''
def clear_table(conn, table : str):
    sql = ' DELETE FROM ' + table + ';'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

'''
    This function print a table in the database.
'''
def print_table(conn, table : str):
    sql = ' SELECT * FROM ' + table + ';'
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)

if "__main__" == __name__:
    main()
    pass
