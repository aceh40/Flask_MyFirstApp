
def sampleContent():
    topic_dict = {"Python Basics":[["Introduction to Python", "/introduction-to-python/"],
                                   ["Print functions and strings", "/print-functions-and-strings/"],
                                   ["Simple number operations", "/simple-number-operations/"]
                                   ],
                    "HTML Basics": [["Introduction to HTML", "/introduction-to-html/"],
                                    ["Basic HTML tags", "/basic-html-tags/"],
                                    ["Jinja variables and logic","/jinja-variables-and-logic/" ]
                                    ]
                } 
    return topic_dict

def blogsFunction():
    blogs = [
        {
             "id": 1,
             "title": 'First blog',
             "body": 'Lorem Ipsum е елементарен примерен текст, използван в печатарската и типографската индустрия.',
             "author": 'Assen',
             "createDate": '2017-12-02'
        },
        {
             "id": 2,
             "title": 'Second blog',
             "body": 'Lorem Ipsum е еле"ментарен примерен текст, използван в печатарската и типографската индустрия.',
             "author": 'Ana',
             "createDate": '2017-12-02'   
        },
        {
             "id": 3,
             "title": 'Third blog',
             "body": 'Lorem Ipsum е елементарен примерен текст, използван в печатарската и типографската индустрия.',
             "author": 'Assen',
             "createDate": '2017-12-02'   
        }
    ]
    return blogs