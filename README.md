# Pythonian

A python program that converts functions to define the NFL QB passer rating calculation using components including:
attempts, completions, yards, touchdowns, and interceptions.

Class

The class of Favorite QB was created to serve as an example of a class that would benefit from this program. 
For example, Aaron Rodges was initialzed as the primary.

Functions

There are 4 other formulas (a, b, c, d) that all use the components "att, comp, yds, td, intcp" that affect the final passing rating formula.
  All calculations required minimum and maximum paramaters of 0 and 2.375 for each component of the passer rating.
  If the result of any calculation is greater than 2.375, it is set to 2.375. If the result is a negative number, it is set to zero.
  
Test

The pytest was done using Aaron Rodger's regular seasons stats from 2005-2009. Test has proven to be successful as it has accurately calculated the correct passer rating for each of the experminented seasons. 

The program is a success and can be used for thorough data analayis, incuding but not limited to; the max, min, highest rated QBs, QB comparison, etc..
 
