let fr = ["apple", "banana", "mango"];

fr.forEach((item, index, arr) => {
    arr[index] = item.toUpperCase();
});

fr.forEach(item => console.log(item));
