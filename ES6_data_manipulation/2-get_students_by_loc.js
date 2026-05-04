export default function getListStudentsByLocation(arr, city) {
    if (!Array.isArray(arr)) {
        return [];
    }
    return arr.filter((student) => student.location === city);
}