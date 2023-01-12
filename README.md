# The problem 🧮

I've been recently asked by a friend in a an educational institution to help out saving their collected phone numbers (which they have in an excel sheet) to a smartphone.
The problem was that they want to`bulk save`so they can save the hundred of numbers they have without wasting the manpower.
Their IT guy tried to use automated solutions for that but the problem was that every contact name was saved as `"?????? ???"`.
This was a result of the contacts being in the Arabic language and the program assuming all of the users would prefer to save contacts in Latin/English letters.


# The solution! ✅

As a lazy-techie guy, I started looking for an already-existed solutions confidently relying on my so-called "advanced googling skills". The result was impressive though, 9 searching hours = 0 solutions🙂.
This is the moment I knew that I have to get my hands dirty... so I did...
🥁🥁🥁
After probably an hour and like 30 lines of code or something it was ready, it was THIS SIMPLE.

## Instructions 🧑‍🏫

nothing special, only have your `.xls`file in the same folder with the script while maintaining the same form as in example `contacts.xls`file provided in repo (you can edit it as well).
also make sure you type the contact phone number without any `+` sign or leading zeros `00` , just the international code followed by number.

> example:
	> 9639xxxxxxxx //syrian number
>
after running script, you can  see your final `.vcf` file there, ready to transfer to your mobile, enjoy your fully functional vCard Arabic file!