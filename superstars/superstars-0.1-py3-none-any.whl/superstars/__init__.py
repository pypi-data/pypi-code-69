import random

def get():

    stars = ["Ranbir Kapoor","Aamir Khan"
"Aarun Nagar",
"Abhishek Bachchan",
"Abhay Deol.",
"Ananya Panday",
"Abhay Mahajan",
"Ashok Samarth",
"Ammy Virk",
"Aditya Pancholi",
"Aditya Kumar",
"Aftab Shivdasani",
"Aditya Shrivastava",
"Ajay Devgn",
"Ajith Kumar",
"Akkineni Nagarjuna",
"Akshay Kumar",
"Akshaye Khanna",
"Ali Fazal",
"Ali Asgar",
"Amitabh Bachchan",
"Amrinder Gill",
"Anil Kapoor"
"Aniruddh Dave",
"Anupam Kher",
"Arbaaz Khan",
"Arfi Lamba",
"Arjun Kapoor",
"Arjun Rampal",
"Armaan Jain",
"Arshad Warsi",
"Arun Govil",
"Ashish Vidyarthi",
"Ashok Kumar",
"Ashok Saraf",
"Atul Kulkarni",
"Avinash Tiwary",
"Ayushman Khurrana",
"Aditya Seal",
"Anu Kapoor",
"Amjad Khan",
"Arif Zakaria",
"Adil Hussain",
"Amrish Puri",
"A. K. Hangal",
"Atul Agnihotri",
"Asrani",
"Asit Sen",
"Ajit",
"Anang Desai",
"Alok Nath",
"Amol Palekar",
"Aanjjan Srivastav",
"Avtar Gill",
"Annu Kapoor",
"Aasif Sheikh",
"Achyut Potdar",
"Aamir Bashir",
"Akhilendra Mishra",
"Angad Bedi",

"Balraj Sahni",
"Bharat Bhushan",
"Bobby Deol",
"Barun Sobti",
"Boman Irani",
"Brijendra Kala",
"Bilal Amrohi",

"Chandrachur Singh",
"Chunky Pandey",

"Dara Singh",
"Darshan Jariwala",
"Dev Anand",
"Dharmendra",
"Dilip Joshi",
"Dilip Kumar",
"Diljit Dosanjh",
"Dayanand Shetty",
"Danny Denzongpa",
"Divyendu Sharma",
"Dalip Tahil",
"Deepak Tijori",
"Deven Verma",
"Dino Morea",
"Dhumal",
"David",
"Dinesh Hingoo",
"Daya Shankar Pandey",
"Dharmesh Yelande",
"Dilip Prabhavalkar",
"Dulquer Salmaan",
"Dheeraj Dhoopar",

"Emraan Hashmi",

"Farooq Sheikh",
"Fardeen Khan",
"Farhan Akhtar",
"Feroz Khan",
"Fawad Khan",

"Govinda",
"Guru Dutt",
"Girish Kumar",
"Gippy Grewal",
"Gurmeet Choudhary",
"Govind Namdev",
"Gulshan Grover",
"Gajraj Rao",
"Goga Kapoor",

"Harman Baweja",
"Harshvardhan Kapoor",
"Harshvardhan Rane",
"Hrithik Roshan",
"Himanshu Malik",
"Himansh Kohli",
"Himesh Reshammiya",
"Honey Singh",
"Harish Patel",
"Harsh Chhaya",
"Harish Kumar"

"Iftekhar",
"Imran Khan",
"Irrfan Khan",
"Inaamulhaq",
"Inder Kumar",
"Ishaan Khatter",

"Jackie Shroff",
"Jackky Bhagnani",
"Jassie Gill",
"John Abraham",
"Jay Bhanushali",
"Jeetendra",
"Jimmy Shergill",
"Jeevan",
"Joy Mukherjee",
"Javed Jaffrey",
"Jagdeep",
"Johnny Walker",
"Johnny Lever",
"Jugal Hansraj",

"Kamal Haasan",
"Kanhaiyalal",
"Kapil Sharma",
"Karan Patel",
"Karanvir Bohra",
"Karan Johar",
"Karan Singh Grover",
"Karan Grover",
"Karan Wahi",
"Kartik Aaryan",
"Kay Kay Menon",
"Kishore Kumar",
"Kumar Gaurav",
"Kunal Kapoor",
"Karmveer Choudhary",
"Kunal Khemu",
"Kamal Kapoor",
"Kader Khan",
"Kiran Kumar",
"Kabir Bedi",
"Kishore Kumar",
"Kulbhushan Kharbanda",
"Keshto Mukherjee",
"Kanwaljit Singh",

"Laxmikant Berde",
"Lakha Lakhwinder Singh",

"Manish Paul",
"Mukesh Batra",
"Mahipal",
"Mahavir Shah",
"Mammootty",
"Manoj Bajpayee",
"Manoj Kumar",
"Manjot Singh",
"Meiyang Chang",
"Mithun Chakraborty",
"Mohanlal",
"Mohnish Bahl",
"Mohit Marwah",
"Milind Gunaji",
"Manoj Tiwari",
"Manoj Pahwa",
"Mohan Joshi",
"Mukesh Rishi",
"Mohan Agashe",
"Mazhar Khan",
"Mohammed Zeeshan Ayyub",
"Mukul Dev",
"Mehmood",
"Murad",
"Mukri",
"Madan Puri",
"Mac Mohan",
"Mahesh Manjrekar",
"M K Raina",
"Milind Soman",
"Mukesh Khanna",
"Mukri",

"Nana Patekar",
"Nikesh Ram",
"Naseeruddin Shah",
"Nassar",
"Navin Nischol",
"Naved Aslam",
"Nawazuddin Siddiqui",
"Neil Nitin Mukesh",
"Nazir Hussain",
"Nana Palshikar",
"Nitish Bharadwaj",

"Om Prakash",
"Om Puri",
"Omi Vaidya",
"Om Shivpuri",

"Pankaj Tripathi",
"Prithviraj Sukumaran",
"Paresh Rawal",
"Prabhas",
"Pradeep Kumar",
"Pran",
"Pankaj Kapur",
"Prem Chopra",
"Prithviraj Kapoor",
"Pulkit Samrat",
"Puneet Issar",
"Prateik Babbar",
"Priyanshu Chatterjee",
"Priyanshu Painyuli",
"Parmeet Sethi",
"Prakash Raj",

"Parikshat Sahni",
"Piyush Mishra",
"Prabhu Deva",
"Punit Pathak",
"Poonam Pandey",
"Patralekha",

"R. Madhavan",
"Raaj Kumar",
"Rahul Roy",
"Rajat Kapoor",
"Rajit Kapur",
"Raj Kapoor",
"Rajeev Khandelwal",
"Rajendra Kumar",
"Rohan Mehra",
"Rajendranath Zutshi",
"Rajesh Khanna",
"Rajinikanth",
"Rajneesh Duggal",
"Rajkummar Rao",
"Rakesh Bapat",
"Rakesh Roshan",
"Ram Charan",
"Ram Kapoor",
"Rana Daggubati",
"Ranbir Kapoor",
"Randeep Hooda",
"Randhir Kapoor",
"Ranveer Singh",
"Ravi Kishan",
"Rishi Kapoor",
"Riteish Deshmukh",
"Ronit Roy",
"Rohit Roy",
"Rahul Kumar",
"Ravi Dubey",
"Rakesh Bedi",
"Raj Babbar",
"Raj Kiran",
"Rahul Bose",
"Raza Murad",
"Ranjeet",
"Rajpal Yadav",
"Ramesh Deo",
"Rehman",
"Raju Kher",
"Ranvir Shorey",
"Razzak Khan",
"Rajesh Vivek",
"Rahul Dev",
"Raj Zutshi",
"Raghubir Yadav",
"Rajat Bedi",
"Rajendra Gupta",

"Shah Rukh Khan",
"Sanjay Khan",
"Salman Khan",
"Satyen Kappu",
"Sanjeev Kumar",
"Salim Khan",
"Sanjay Dutt",
"Sanjay Kapoor",
"Sanjay Mishra",
"Sanjay Suri",
"Sarath",
"Saif Ali Khan",
"Sushant Singh Rajput",
"Shakti Kapoor",
"Shammi Kapoor",
"Sharman Joshi",
"Shashi Kapoor",
"Shatrughan Sinha",
"Shiney Ahuja",
"Shreyas Talpade",
"Sidhant Gupta",
"Sidharth Malhotra",
"Sidharth Shukla",
"Sikandar Kher",
"Sohail Khan",
"Sonu Sood",
"Sooraj Pancholi",
"Subrat Dutta",
"Sudeep",
"Suniel Shetty",
"Sunny Deol",
"Suresh Oberoi",
"Shahid Kapoor",
"Sunil Dutt",
"Sharad Kapoor",
"Sharad Kelkar",
"Sayaji Shinde",
"Shriram Lagoo",
"Sadashiv Amrapurkar",
"Satyen Kappu",
"Siddharth Ray",
"Sharat Saxena",
"Saeed Jaffrey",
"Sumeet Vyas",
"Sapru",
"Satish Kaushik",
"Sushant Singh",
"Sudesh Berry",
"Sudhir Pandey",
"Sudhir",
"Siddhant Chaturvedi",

"Tiger Shroff",
"Tinnu Anand",
"Tusshar Kapoor",
"Tiku Talsania",
"Tom Alter",
"Tahir Raj Bhasin",
"Trilok Kapoor",

"Upen Patel",
"Utpal Dutt",
"Uttam Kumar",

"Varun Badola",
"Varun Dhawan",
"Varun Mitra",
"Varun Sharma",
"Vicky Kaushal",
"Vidyut Jammwal"
"Vikrant Massey",
"Vinod Khanna",
"Vinod Mehra",
"Vijay Arora",
"Vivaan Shah",
"Vivan Bhatena",
"Vivek Mushran",
"Vivek Oberoi",
"Vikram Gokhale",
"Vijay Raaz",
"Virendra Saxena",
"Vinay Pathak",
"Vijay",

"Waris Ahluwalia",

"Yashpal Sharma",
"Yashmith",

"Zakir Hussain",
"Zayed Khan",
"Zubeen Garg",
"Zareen Khan"]
    print(random.choice(stars))
