def greet(bot_name, birth_year):
    print("Hello! My name is {0}.".format(bot_name))
    print("I was created in {0}.".format(birth_year))


def remind_name():
    print('\nPlease tell me your name.')
    name = input()
    print("What a great name you have, {0}!".format(name))


def dept():
    print('\nDo you want to know about the departments?')
    reply = input()
    while True:
        if reply == 'no':
            return
        elif reply == 'yes' or 'Yes' or 'YES' or 'yup':
            print("Departments in BMSIT\n 1. AIML\n 2. CSE\n 3. ISE\n 4. Mechanical\n 5. Exit")
            choice = int(input("\nEnter the Choice: "))
            if choice == 1:
                print("\nA New Beginning! Artificial Intelligence and Machine Learning Department was formally inaugurated on 02-Aug-2019, in the esteemed presence of our beloved Chairman Sri.\n Madan Gopal, IAS and our visionary leader,\n "
              "Principal Dr. Mohan Babu G N and several other distinguished dignitaries. \n"
              "The event drafted the script for a new chapter in the history of our college to offer an undergraduate program in Artificial Intelligence and Machine Learning, a much sought-after skill set for the future.\n")
            elif choice == 2:
                print("\nComputer Science & Engineering deals with the theoretical foundations of information and computation along with practical techniques for implementation and application.\n "
              "Computer Science engineers can contribute as Software Developers, Hardware Engineers,\n"
              " Database Analysts (SQL), System analysts or System Engineers, Security analysts, Business System Database Developer, Data Modeller, Software Quality Assurance (QA) apart from multi-disciplinary research.\n")
            elif choice == 3:
                print("\nThe Department of Information Science and Engineering started in the Year 2010 with an approved intake of 60\n"
              " and Enhanced to 120 from the academic year 2018-19 and to 180 from the academic year 2019-20.\n "
              "The Department has qualified and professionally dedicated faculty member practice OBE in the academic deliverables. \n"
              "The faculties have published research articles in various National, International, IEEE Conferences, and Journals.\n")
            elif choice == 4:
                print("\nWelcome to the Department of Mechanical Engineering, BMSIT&M. The Department of Mechanical Engineering was established in the year 2002-03. \nThe Department offers full-time UG programme in Mechanical Engineering with an annual intake of 60 students.\n"
              " The programme is affiliated to Visvesvaraya Technological University (VTU), Belagavi and approved by All India Council for Technical Education (AICTE). \n"
              "The UG programme is provisionally accredited by the National Board of Accreditation (NBA), New Delhi and also Permanently Affiliated to Visvesvaraya Technological University (VTU), Belagavi.\n")
            elif choice == 5:
                break
            else:
                print("Please Provide a valid Input!\n")

def map():
    print('\nDo you want to know location of BMSIT?')
    map = input()
    if map == 'no':
        return

    if map == 'yes' or 'Yes' or 'YES' or 'yup':
        print('Doddaballapur Main Road, Avalahalli, Yelahanka, Bengaluru, Karnataka 560064\n')


def phno():
    print('\nDo you want to know the contact details of BMSIT?')
    phno = input()
    if phno == 'no':
        return

    if phno == 'yes' or 'Yes' or 'YES' or 'yup':
        print('\n080 28561576')
        print('Email: principal@bmsit.in\n')


def add():
    print('\nDo you want to know the admission details of BMSIT?')
    reply = input()
    if reply == 'no':
        return

    if reply == 'yes' or 'Yes' or 'YES' or 'yup':
        print('')
        print('Admission Queries : 080 - 68730429')
        print('Fee Queries : 080 - 68730428')
        print('Hostel Queries : 9739947120 / 7483394536 / 9741590336')
        print('Others : 080-29521171 / 080 - 68730444\n')
        print('Number of UG students = 3250+')
        print('Number of faculty = 275+')
        print('Number of company visits = 150+\n')

def end():
    print('\nThank you for conversing with me , have a nice day!\n')
    input()

def placement():
    print('\nDo you want to know the placement details of BMSIT?')
    reply = input()
    if reply == 'no':
        return

    if reply == 'yes' or 'Yes' or 'YES' or 'yup':
        print('')
        print('Total number of company visits : 120')
        print('Highest CTC Offered in INR : 26.5 LPA')
        print('Average CTC Offered in INR : 6.62 LPA')
        print('Number of Eligible & Interested UG Students : 508\n')
        print('Number of Students Placed : 410')
        print('% of Eligible Students Placed : 80.71%')
        print('Total Number of Offers Received : 595')
        print('Total Number of Paid Internship offers : 293')
        print('Internship Stipend Range in INR per Month : 10K to 50K\n')
        print('* Placement is in progress for 2020-21 Batch\n')

greet('BMSIT Bot', '2022')
remind_name()
add()
dept()
placement()
map()
phno()
end()
