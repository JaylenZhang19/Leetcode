/**
 * // This is the robot's control interface.
 * // You should not implement it, or speculate about its implementation
 * class Robot {
 *   public:
 *     // Returns true if the cell in front is open and robot moves into the cell.
 *     // Returns false if the cell in front is blocked and robot stays in the current cell.
 *     bool move();
 *
 *     // Robot will stay in the same cell after calling turnLeft/turnRight.
 *     // Each turn will be 90 degrees.
 *     void turnLeft();
 *     void turnRight();
 *
 *     // Clean the current cell.
 *     void clean();
 * };
 */

class Solution {
public:
    
    vector<vector<int>> directions = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    set<pair<int, int>> visited;
    
    void goBack(Robot& robot) {
        robot.turnRight();
        robot.turnRight();
        robot.move();
        robot.turnRight();
        robot.turnRight();
    }
    
    void backtrack(Robot& robot, int row, int col, int d) {
        visited.insert(pair<int, int>(row, col));
        robot.clean();
        
        for (int i = 0; i < 4; ++i) {
          int newD = (d + i) % 4;
          int newRow = row + directions[newD][0];
          int newCol = col + directions[newD][1];
          if ( (visited.find(pair(newRow, newCol)) == visited.end())
               && robot.move()) {
            backtrack(robot, newRow, newCol, newD);
            goBack(robot);
          }
          robot.turnRight();
        }
    }

    void cleanRoom(Robot& robot) {
        backtrack(robot, 0, 0, 0);
    }
};