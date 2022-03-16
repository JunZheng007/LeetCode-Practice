/*
 * @lc app=leetcode id=207 lang=typescript
 *
 * [207] Course Schedule
 */
// @lc code=start
function canFinish(numCourses, prerequisites) {
    var indexs = Array(numCourses).fill(false);
    var current = prerequisites[0];
    var i = 0;
    console.log(current, indexs);
    while (!indexs[i]) {
        prerequisites.forEach(function (value, index) {
            if (value[0] == current[1]) {
                console.log(value, current);
                current = value;
                indexs[index] = true;
                i = index;
                return;
            }
        });
        console.log(current, indexs);
    }
    return false;
}
;
// @lc code=end
