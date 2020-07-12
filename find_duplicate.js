#!/usr/bin/env node

console.log('I choose this way to solve this issue, because a duplicate number can be in one half of an array with a compared number, so if we check both halves one by one we can find a duplicate there and don\'t require to check other numbers. And only if we don\'t find it there we\'ll check remaining numbers.');

const numbers = [51942, 392852, 172619, 139355, 28381, 3928, 234440, 373913, 460289, 303789, 484186, 20632, 167950, 335145, 438067, 139315, 320884, 225265, 362652, 261904, 34691, 312844, 336891, 80380, 480140, 259648, 465812, 298404, 474816, 214744, 491022, 133437, 164088, 371300, 5611, 245466, 472565, 206750, 326367, 483719, 483965, 237329, 308983, 193565, 178730, 287975, 199132, 147760, 295727, 183524, 429357, 41165, 59207, 470356, 200792, 454935, 486067, 269581, 289976, 481827, 15011, 470890, 412461, 434381, 498198, 63077, 138582, 52103, 5943, 498150, 160477, 398919, 444071, 79756, 92069, 227515, 56229, 265830, 465036, 157, 297063, 80275, 319631, 148486, 468307, 243391, 337656, 280125, 8488, 360704, 312541, 48854, 140113, 404870, 193253, 386113, 315277, 421925, 283958, 202471, 51942];


const llen = numbers.length;
const median_index = Math.floor(llen / 2);

let duplicate;

function compareValuesInOnePart(array, range_start, range_end) {
    for (let i = range_start; i <= range_end; i++) {
        for (let j = i + 1; j <= range_end; j++) {
            if (array[i] === array[j]) {
                return array[i];
            }
        }
    }
    return false;
}

function compareValuesInTwoParts(array, range_end, length) {
    for (let i = 0; i <= range_end; i++) {
        for (let j = range_end + 1; j <= length; j++) {
            if (array[i] === array[j]) {
                return array[i];
            }
        }
    }
    return false;
}

const duplicate1 = compareValuesInOnePart(numbers, 0, median_index, median_index);

duplicate = duplicate1;

if (!duplicate1) {
    const duplicate2 = compareValuesInOnePart(numbers, median_index + 1, llen, llen);
    duplicate = duplicate2;
    if (!duplicate2) {
        const duplicate3 = compareValuesInTwoParts(numbers, median_index, llen);
        duplicate = duplicate3;
    }
}

if (duplicate) {
    console.log('Duplicate number is ' + duplicate);
} else {
    console.log('There is no duplicates.');
}
