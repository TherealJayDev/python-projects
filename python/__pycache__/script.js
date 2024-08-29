
let grades = {
    'John': [90, 95, 98],
    'Eric': [86, 84, 92],
    'Michael': [90, 89, 85]
};
//  This grade book is an object that consists of the student's name as the key, and the value is a list representing results for a series of tests, from most recent to oldest.
//  A new exam has just been graded, and you receive the grades for that specific exam also as an object:
let exam = {
    'Eric': 99,
    'John': 100
};
//  Write code that updates the grades object by adding the latest test result to the beginning of each list corresponding to the student.

//  If the new exam grade is missing for a student, assign the value `None` as the latest grade in the `grades` object.
//  For the data given above, your `grades` object should now contain the following information:

 
//  {
    //  'John': [100, 90, 95, 98],
    //  'Eric': [99, 86, 84, 92],
    //  'Michael': [None, 90, 89, 85]
//  }

// inputs are grades object and exam object

function addGrade(gradesObj, examObj) {
    const keys = Object.keys(grades)
    const values = Object.values(grades)

    console.log(keys, values)
}

addGrade(grades, exam)

// convert the grades object to an array of keys and values
// loop over items in the grades object
// access grade in exam oject using the keys of the grades object
// add the value of the items in the exam object to the matching array of the grades object
//  return the grades object with the new data


 