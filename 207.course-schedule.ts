/*
 * @lc app=leetcode id=207 lang=typescript
 *
 * [207] Course Schedule
 */

// @lc code=start
function canFinish(numCourses: number, prerequisites: number[][]): boolean {
    // const indexs: boolean[] = Array(numCourses).fill(true);
    // let current = prerequisites[0];
    // let i = 0;
    // indexs[0] = true;
    // console.log(current, indexs);

    for (let i = 0; i < numCourses; i++) {
        const courses = [i];
        while (courses.length <= numCourses) {
            console.log(courses);
            
            const preCourse = prerequisites.find(c => c[0] === courses[courses.length - 1]);
            
            
            if (preCourse) {
                if (courses.find(c => c === preCourse[1])) {
                    return false;
                }
                courses.push(preCourse[1]);
            }
            else {
                break;
            }
            console.log(courses, preCourse);
        }
    }

    // while (!indexs[i]) {
    //     let next = i;
    //     prerequisites.forEach((value, index) => {
    //         if (value[0] === current[1] && !indexs[index]) {
    //             console.log(value, current);
    //             current = value;
    //             indexs[index] = true;
    //             next = index;
    //             return
    //         }
    //     })
    //     console.log(current, indexs);
    //     if (next === i) {
    //         break;
    //     }
    // }
    return true;
};
// @lc code=end

console.log(canFinish(2, [[1, 0]]));