// https://launchschool.com/lessons/bfc761bc/assignments/ff1533e4

let studentScores = {
  student1: {
    id: 123456789,
    scores: {
      exams: [90, 95, 100, 80],
      exercises: [20, 15, 10, 19, 15],
    },
  },
  student2: {
    id: 123456799,
    scores: {
      exams: [50, 70, 90, 100],
      exercises: [0, 15, 20, 15, 15],
    },
  },
  student3: {
    id: 123457789,
    scores: {
      exams: [88, 87, 88, 89],
      exercises: [10, 20, 10, 19, 18],
    },
  },
  student4: {
    id: 112233445,
    scores: {
      exams: [100, 100, 100, 100],
      exercises: [10, 15, 10, 10, 15],
    },
  },
  student5: {
    id: 112233446,
    scores: {
      exams: [50, 80, 60, 90],
      exercises: [10, 0, 10, 10, 0],
    },
  },
};

function getGrade(grade) {
  if (grade >= 93 && grade <= 100) {
    return 'A';
  } else if (grade >= 85 && grade <= 92) {
    return 'B';
  } else if (grade >= 77 && grade <= 84) {
    return 'C';
  } else if (grade >= 69 && grade <= 76) {
    return 'D';
  } else if (grade >= 60 && grade <= 68) {
    return 'E';
  } else {
    return 'F';
  }
}

function buildMap(scores) {
  const examMap = new Map([['exam1', []], ['exam2', []], ['exam3', []], ['exam4', []]]);

  scores.forEach(student => {
    let exam = student.scores.exams;
    examMap.get('exam1').push(exam[0]);
    examMap.get('exam2').push(exam[1]);
    examMap.get('exam3').push(exam[2]);
    examMap.get('exam4').push(exam[3]);
  });

  return examMap;
}

function formatExams(examMap) {
  let exams = [];

  for (let examArray of examMap.values()) {
    exams.push({
      average: examArray.reduce((exams, grade) => exams + grade) / 5,
      minimum: Math.min(...examArray),
      maximum: Math.max(...examArray),
    })
  }

  return exams;
}

function generateClassRecordSummary(scores) {
  const arrayScores = Object.values(scores);
  const EXAM_WEIGHT = 0.65;
  const EXERCISE_WEIGHT = 0.35;
  const examMap = buildMap(arrayScores);

  let studentNumberGrades = arrayScores.map(student => {
    let averageExamGrade = Math.round(student.scores.exams.reduce((examGrade, exam) => examGrade + exam) / 4);
    let averageExercisesGrade = Math.round(student.scores.exercises.reduce((exerciseGrade, exercises) => exerciseGrade + exercises));
    let finalGrade = Math.round((averageExamGrade * EXAM_WEIGHT) + (averageExercisesGrade * EXERCISE_WEIGHT));
    return finalGrade;
  });

  let formattedStudentGrades = studentNumberGrades.map(grade => {
    let letterGrade = getGrade(grade);
    return `${grade} (${String(letterGrade)})`;
  })

  return {
    studentGrades: formattedStudentGrades,
    exams: formatExams(examMap),
  }
}

console.log(generateClassRecordSummary(studentScores));


// returns:
/*
output: object that has studentGrades and exams;
studentGrades. - array of 5 student grades
exams - array of objects, objects hold average min and max of each exam

*/
// {
//   studentGrades: [ '87 (B)', '73 (D)', '84 (C)', '86 (B)', '56 (F)' ],
//   exams: [
//     { average: 75.6, minimum: 50, maximum: 100 },
//     { average: 86.4, minimum: 70, maximum: 100 },
//     { average: 87.6, minimum: 60, maximum: 100 },
//     { average: 91.8, minimum: 80, maximum: 100 },
//   ],
// }


'use strict';

/*
input: object -> student object inside,
output: object -> studentGrades: (array (strings)), exams: (array of objects)
rules:
1. Exam weight is 65%
  a. 4 exams
  b. max score is 100.
2. Exercises weight is 35%
  a. varied score values and counts
  b. total max point value is 100. Regardless of how many exercises completed
    ii. [20,30,50] = 100
3. Get student's grade
  a. Average score of the four exams,
  b. Sum all exercise scores.
  c. apply weight to compute student's final percent grade.
4. Grading chart.

Questions:
1. Rounding integer do we round up only if its .5 and up? And then down if its .4 and lower?




DS:
1. An array to compute studentScores

Algo:
1. Create function that gives letter grade based on exam
2. Convert input into an array
  a. variable to access exams
  b. variable to access exercises
3. Function to find avg, max, min -> pass an array of student exams
  1. return average
  2. return min
  3. return max
4. Function to find total of exercises
5. Main function compute the weight of the grade
  a. use the weight to call function to get letter grade.



*/

let studentScores = {
  student1: {
    id: 123456789,
    scores: {
      exams: [90, 95, 100, 80],
      exercises: [20, 15, 10, 19, 15],
    },
  },
  student2: {
    id: 123456799,
    scores: {
      exams: [50, 70, 90, 100],
      exercises: [0, 15, 20, 15, 15],
    },
  },
  student3: {
    id: 123457789,
    scores: {
      exams: [88, 87, 88, 89],
      exercises: [10, 20, 10, 19, 18],
    },
  },
  student4: {
    id: 112233445,
    scores: {
      exams: [100, 100, 100, 100],
      exercises: [10, 15, 10, 10, 15],
    },
  },
  student5: {
    id: 112233446,
    scores: {
      exams: [50, 80, 60, 90],
      exercises: [10, 0, 10, 10, 0],
    },
  },
};

/*
Algo:
1. Create function that gives letter grade based on exam
2. Convert input into an array
  a. variable to access exams
  b. variable to access exercises
3. Function to find avg, max, min -> pass an array of student exams
  1. return average
  2. return min
  3. return max
4. Function to find total of exercises
5. Main function compute the weight of the grade
  a. use the weight to call function to get letter grade.



*/

// Second way i did it

// function generateClassRecordSummary(scores) {
//   let studentScores = Object.keys(scores).map(student => scores[student].scores);
//   let examData = studentScores.map(score => score.exams);

//   let allStudentGrades = studentScores.map(data => {
//     let examGrades = getExamAverage(data.exams);
//     let exerciseGrades = totalExerciseScore(data.exercises);
//     let percentGrade = Math.round((examGrades * .65) + (exerciseGrades * .35));
//     return `${percentGrade} (${getGrade(percentGrade)})`;
//   });

//   let allExams = computeExams(examData);

//   return {
//     studentGrades: allStudentGrades,
//     exams: allExams,
//   };
// }

// function getExamAverage(examArray) {
//   return examArray.reduce((sum, exam) => sum + exam, 0) / 4;
// }


// function getGrade(gradeScore) {
//   if (93 <= gradeScore && gradeScore <= 100) {
//     return 'A';
//   } else if (85 <= gradeScore && gradeScore <= 92) {
//     return 'B';
//   } else if (77 <= gradeScore && gradeScore <= 84) {
//     return 'C';
//   } else if (69 <= gradeScore && gradeScore <= 76) {
//     return 'D';
//   } else if (60 <= gradeScore && gradeScore <= 68) {
//     return 'E';
//   } else {
//     return 'F';
//   }
// }

// function computeExams(examData) {
//   let examArray = Array.from({length : 4}, () => []);
//   examData.forEach(exams => exams.forEach((exam, index) => examArray[index].push(exam)));

//   return examArray.map(exam => {
//     return {
//       average: findAverage(exam),
//       minimum: Math.min(...exam),
//       maximum: Math.max(...exam),
//     };
//   });
// }

// function findAverage(exams) {
//   return exams.reduce((sum, exam) => sum + exam, 0) / 5;
// }

// function totalExerciseScore(studentExercises) {
//   return studentExercises.reduce((sum, exercise) => sum + exercise, 0);
// }

// console.log(generateClassRecordSummary(studentScores));

// // returns:
// // {
// //   studentGrades: [ '87 (B)', '73 (D)', '84 (C)', '86 (B)', '56 (F)' ],
// //   exams: [
// //     { average: 75.6, minimum: 50, maximum: 100 },
// //     { average: 86.4, minimum: 70, maximum: 100 },
// //     { average: 87.6, minimum: 60, maximum: 100 },
// //     { average: 91.8, minimum: 80, maximum: 100 },
// //   ],
// // }