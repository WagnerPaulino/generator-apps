export default class Utils {

    isNull(value, nullble) {
        if (value === null || value === undefined) {
            return nullble;
        } else {
            return value;
        }
    }
}