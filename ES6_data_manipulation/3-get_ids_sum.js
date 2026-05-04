export default function getStudentsIdsSum(arr) {
    if (!Array.isArray(arr)) {
        return [];
    }
    return arr.reduce((sum, student) => sum + student.id , 0);
}