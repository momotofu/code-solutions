#include <stdio.h>
enum indexes{currentDirection, pen, currentRow, currentColumn};
enum compass{UP,RIGHT,DOWN,LEFT};
const int gridSize = 80; // Array Floor Size.
const int strokeLength = 10;

int gameRunning = 1;
void input(int *inputArray , char gameFloor[gridSize][gridSize], int command);
void clearFloor(char gameFloor[gridSize][gridSize]);
void displayFloor(char gameFloor[gridSize][gridSize]);
void move(int inputArray[], char gameFloor[gridSize][gridSize], int distance);

int main(){
    int i, j;
    int inputArray[4]={1,1,0,0};
    char gameFloor[gridSize][gridSize];

    // clear gameFloor
    input(inputArray, gameFloor, 7);

    // DRAW I CHARACTER
    // Draw top stroke
    input(inputArray, gameFloor, 1);
    move(inputArray, gameFloor, strokeLength);

    // Draw middle stroke
    input(inputArray, gameFloor, 2); // pun up
    input(inputArray, gameFloor, 4);
    input(inputArray, gameFloor, 4);// turn around
    move(inputArray, gameFloor, strokeLength / 2);
    input(inputArray, gameFloor, 1); // pen down
    input(inputArray, gameFloor, 4); // point down
    move(inputArray, gameFloor, strokeLength);

    // Draw bottom stroke
    input(inputArray, gameFloor, 2); // pun up
    input(inputArray, gameFloor, 3); // turn right
    move(inputArray, gameFloor, strokeLength);
    input(inputArray, gameFloor, 1); // pun down
    input(inputArray, gameFloor, 4); // turn right
    input(inputArray, gameFloor, 4); // turn right
    move(inputArray, gameFloor, strokeLength);

    // Draw a space
    input(inputArray, gameFloor, 2); // pen up
    move(inputArray, gameFloor, strokeLength);

    // DRAW M CHARACTER
    // draw stroke up
    input(inputArray, gameFloor, 4); // point up
    input(inputArray, gameFloor, 1); // pen down
    move(inputArray, gameFloor, strokeLength);

    // draw stroke right
    input(inputArray, gameFloor, 3); // point right
    move(inputArray, gameFloor, strokeLength);

    // draw stroke down
    input(inputArray, gameFloor, 3); // point down
    move(inputArray, gameFloor, strokeLength);

    // reverse
    input(inputArray, gameFloor, 4);
    input(inputArray, gameFloor, 4);
    move(inputArray, gameFloor, strokeLength); // move up
    input(inputArray, gameFloor, 3);
    move(inputArray, gameFloor, strokeLength); // draw stroke right
    input(inputArray, gameFloor, 3);
    move(inputArray, gameFloor, strokeLength);

    // Draw a space
    input(inputArray, gameFloor, 2); // pen up
    input(inputArray, gameFloor, 4); // pen up
    move(inputArray, gameFloor, strokeLength);

    // DRAW U CHARACTER
    input(inputArray, gameFloor, 1); // pen down
    input(inputArray, gameFloor, 4); // point up
    move(inputArray, gameFloor, strokeLength);
    input(inputArray, gameFloor, 4);
    input(inputArray, gameFloor, 4);
    move(inputArray, gameFloor, strokeLength);
    input(inputArray, gameFloor, 4);
    move(inputArray, gameFloor, strokeLength);
    input(inputArray, gameFloor, 4);
    move(inputArray, gameFloor, strokeLength);

    // print out the gameFloor
    input(inputArray, gameFloor, 6);
    input(inputArray, gameFloor, 8);
    return 0;
}

void clearFloor(char gameFloor[gridSize][gridSize]){
int row,column;
for(row=0; row < gridSize ; row++){
    for(column = 0;column < gridSize ; column++){
        gameFloor[row][column]= ' ';//set to 0 for debug
        }
    }
}

void displayFloor(char gameFloor[gridSize][gridSize]){
    int row,column;
    for(row= 0 ; row < gridSize ; row++){
        for(column=0 ; column < gridSize ; column++){
        printf("%c", gameFloor[row][column] );
    }
      printf("\n");
    }
}

// void input(int inputArray[] , char gameFloor[gridSize][gridSize], int command){
void input(int *inputArray, char gameFloor[gridSize][gridSize], int command){
    int distance;
    switch(command){
    case 1:
        inputArray[pen]=1;
        break;
     case 2:
        inputArray[pen]=0;
        break;
    case 3:
        if(inputArray[currentDirection] < 3){
            inputArray[currentDirection]++;
        } else {
            inputArray[currentDirection] = RIGHT;
        }
        break;
    case 4:
        if(inputArray[currentDirection] > 0){
            inputArray[currentDirection]--;
        }
        else{
            inputArray[currentDirection] = LEFT;
        }
        break;
    case 5:
        move(inputArray, gameFloor, distance);
        break;
    case 6:
        displayFloor(gameFloor);
        break;
    case 7:
        clearFloor(gameFloor);
    break;
    case 8:
        printf("Exiting Now");
        break;
    }
}

void move(int *inputArray,char gameFloor[gridSize][gridSize], int distance){
    int i;
    printf("Move called with direction %d\n", inputArray[currentDirection]);
    printf("Pen value is %d\n", inputArray[pen]);
    printf("CurrentRow %d, currentColumn %d\n", inputArray[currentRow], inputArray[currentColumn]);

   switch(inputArray[currentDirection]){
      case UP:
          distance = inputArray[currentRow] - distance;
          if(distance < 0){//Turtle doesnt move if the amount of distance that user specified would put it outside of the grid.
              distance = 0;
          }
          if(inputArray[pen] == 1){//Copy Paste pen function for if drawing is TRUE / pen is down
              for(i = inputArray[currentRow] ; i >= distance; i--){//Moving up will always be a negative shift in the "compass" system.
                  gameFloor[i][inputArray[currentColumn]] = '*';
                  inputArray[currentRow] = i;
                  }
          }
          else{
              inputArray[currentRow] = distance;//Else move the distance but do not print *
          }
          break;//End Case

      case RIGHT:
          distance = inputArray[currentColumn] + distance;
          if(distance > gridSize - 1){
          distance = gridSize - 1;
          }
          if(inputArray[pen] == 1){
              for(i=inputArray[currentColumn];i<=distance;i++){
                  gameFloor[inputArray[currentRow]][i] = '*';
              }
          }
          inputArray[currentColumn] = distance;

          break;

      case DOWN:
          distance = inputArray[currentRow] + distance;
          if(distance > gridSize - 1){
              distance = gridSize - 1;
          }
          if(inputArray[pen] == 1){
              for(i = inputArray[currentRow]; i<=distance; i++){
                  gameFloor[i][inputArray[currentColumn]] = '*';
                  inputArray[currentRow] = i;
              }
          }//possible else here if debugging issue isnt fixed
          inputArray[currentRow] = distance;

          break;

      case LEFT:
          distance = inputArray[currentColumn] - distance;
          if(distance<0)
          {
              distance=0;
          }
          if(inputArray[pen] == 1){
              for(i = inputArray[currentColumn]; i >= distance ; i--){
                  gameFloor[inputArray[currentRow]][i] = '*';
              }
          }
          inputArray[currentColumn]=distance;
          break;
  }
}
