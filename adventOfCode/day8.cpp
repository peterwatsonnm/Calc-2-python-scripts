//advent of code day 8
//author: Peter Watson

#include <iostream>
using namespace std;
#include <string>
#include <fstream>

/*
algorithm:

create a string with the integers in it
get the first 6 characters
store in an array
go to next 6 characters
store in array until arrayHeight rows are created
move to next layer

3d array with 100 on z axis, 25 on x and 6 on y
*/


int main(){
  const int arrWidth = 25;
  const int arrHeight = 6;
  const int numLayers = 100;
  const string black = "0";
  const string white = "1";
  const string transparent = "2";
  string arr[arrHeight][arrWidth][numLayers];   //is one since each arrWidth sized chunk is represented as one integer
  string filename = "transmission.txt";
  string tempString;
  //string widthString = "";
  int index = 0;
  int zeroCount = 0;
  int oneCount = 0;
  int twoCount = 0;
  int tempOneCount = 0;
  int tempTwoCount = 0;
  int bestLayer;
  int min = (arrWidth * arrHeight) + 1;   //any number of 0s will be less than this
  ifstream file(filename);
  if (!file.is_open())
  {
    cout << "error";
    return 0;
  }
  getline(file, tempString);
  //cout << "tempString: " << tempString << endl;

  for (int i = 0; i < numLayers; i++)
  {
    //create one layer
    for (int j = 0; j < arrHeight; j++)
    {
      //get arrWidth characters from tempString
      for (int n = 0; n < arrWidth; n++)
      {
        //index indicates how many arrWidth chunks have been read already
        arr[j][n][i] = tempString[(arrWidth * index) + n];    //arrWidth * index ensures that program will go through the string in chunks of size arrWidth
        if (tempString[(arrWidth * index) + n] == '0')   //if character is 0
        {
          zeroCount ++;
        }
        if (tempString[(arrWidth * index) + n] == '1')
        {
          tempOneCount ++;
        }
        if (tempString[(arrWidth * index) + n] == '2')
        {
          tempTwoCount++;
        }
      }
      //arr[j][0][i] = (widthString);
      index ++;
      //widthString = "";
    }
    //one layer is created
    //check how many zeros it has, and if it is new min, set it to min
    //cout << "zero count for layer " << i << ": " << zeroCount << endl;
    if (zeroCount < min)
    {
      bestLayer = i;
      min = zeroCount;
      //these values are saved if the layer is the min layer
      oneCount = tempOneCount;
      twoCount = tempTwoCount;
    }
    zeroCount = 0;
    tempOneCount = 0;
    tempTwoCount = 0;   //reset temp counters
  }

  //PRINT THE MESSAGE:
  //go through each line
  //zero in on the first character
  //go through the layers, and stop when a non-transparent layer is reached
  //cout that character
  //move to next character

  for (int i = 0; i < arrHeight; i++)
  {
    for (int j = 0; j < arrWidth; j++)
    {
      for (int n = 0; n < numLayers; n++)
      {
        if (arr[i][j][n] != transparent)
        {
          //print the character if it is not transparent
          if (arr[i][j][n] == black)
          {
            cout << " ";
          }
          else
          {
            cout << arr[i][j][n];

          }
          break;    //stop searching because non transparent character was reached
        }
      }
    }
    cout << endl;   //next line
  }

  cout << "best layer : " << bestLayer << endl;
  cout << "Answer: " << oneCount * twoCount << endl;
  return 0;
}
