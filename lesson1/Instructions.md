### Pattern formation

In the eralier example, we formed the following patterns using for `loop` and `if else` clause.

`c = 5`

```
* 
* *
* * * 
* * * * 
* * * * * 
```

Reverse

```
        *
      * *
    * * * 
  * * * * 
* * * * * 
```

In the next exercise please form the following patters using `loops` and `if else` statements.

1) Pyramid: `c = 5`

```
    *
   * *
  * * *
 * * * *
* * * * *
```

2) Diamond: `c = 5`

```
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
```

3) Bonus: Reverse Diamond: `c = 5`

```
*        * 
* *      * * 
* * *    * * * 
* * * *  * * * * 
* * * * * * * * *  
* * * *  * * * * 
* * *    * * * 
* *      * * 
*        * 
```


**Note** The minimum value for `c` is `5`!


Tips
- You can use multiplication if you want
- Make sure to remember the manual solving (in paper) that I showed you before. USE PEN AND PAPER

Submission details:
- Create a file `exer1.py` or `exer1.js`
- If you wish to submit individual work, please put `exer1_<name>` in the file name.

Format shoud be like this


```python
# For python
number = 5

def pyramid(c=5):
	print('\n\n')
	print('== Pyramid ==')
	# do your code here
	return

def diamond(c=5):
	print('\n\n')
	print('== Diamond ==')
	# do your code here
	return


def bonus(c=5):
	print('\n\n')
	print('== Bonus ==')
	# do your code here
	return

pyramid(number)
diamond(number)
bonus(number)

```


```java
var number = 5;

function pyramid(c) {
	console.log('\n\n');
	console.log('== Pyramid ==');
	// do your code here
}

function diamond(c) {
	console.log('\n\n');
	console.log('== Diamond ==');
	// do your code here
}


function bonus(c) {
	console.log('\n\n');
	console.log('== Bonus ==');
	// do your code here
}

pyramid(number);
diamond(number);
bonus(number);

```

Put your submissions in your respective folder.

- `git add .`
- `git commit -am 'Exer 1 submission'`
- `git push`

You can run these commands to submit.