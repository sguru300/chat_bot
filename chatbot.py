<?xml version="1.0" encoding="UTF-8"?>
<aiml>
   <category>
        <pattern>* are you</pattern>
        <template>
            i am a harry potter conversing bot
        </template>
    </category>
    <category>
        <pattern>_ name</pattern>
        <template>
            i am lord voldemort
        </template>
    </category>
     <category>
        <pattern>hey</pattern>
        <template>
            hello to you to!!
        </template>
    </category>
     <category>
        <pattern>hi *</pattern>
        <template>
            hello to you to!!
        </template>
    </category>
    
    <category>
        <pattern>hello </pattern>
        <template>
            hello to you to!!
        </template>
    </category>
 <category>
        <pattern>who is your favorite character</pattern>
        <template>
            <random>
            <li>harry potter. what about you?</li>
            <li>ron weasley. what about you?</li>
            <li>albus dumbledore. what about you?</li>
            <li>severus snape. what about you?</li>
            <li>hermione. what about you?</li>
        </random>
        </template>
    </category>
<category>
      <pattern>my favorite character is *</pattern>
      <template>
         its nice that your favorite character is <set name="charac"><star/></set>
      </template>  
   </category>  
   <category>
      <pattern>what is my favorite characters name</pattern>
      <template>
         Your favorite characters name is name is <get name="charac"/>.
      </template>  
   </category>  
   
    
    <category>
        <pattern>who wrote *</pattern>
        <template>
            im guessing it is JK Rowling
        </template>
    </category>
 <category>
        <pattern>* house *</pattern>
        <template>
            i think it is gryffindor
        </template>
    </category>
    <category>
<pattern>love</pattern> 
<template> well i just love the harry potter series </template>
</category>

<category>
<pattern>_ love</pattern> 
<template><srai>love</srai></template>
</category>

<category>
<pattern>love _</pattern>
<template><srai>love</srai></template>
</category>

<category>
<pattern>_ love *</pattern>
<template><srai>love</srai></template>
</category>

<category>
<pattern>info</pattern> 
<template> please visit www.harrypotter.com </template>
</category>

<category>
<pattern>_ info</pattern> 
<template><srai>info</srai></template>
</category>

<category>
<pattern>info _</pattern>
<template><srai>info</srai></template>
</category>

<category>
<pattern>_ info *</pattern>
<template><srai>info</srai></template>
</category>

<category>
<pattern>who is *</pattern>
<template>someone important in the harry potter series of course.</template>
</category>
<category>
<pattern>why *</pattern>
<template>just ask that to JK Rowling</template>
</category>
<category>
<pattern>what *</pattern>
<template>if you dont know, then you aren't a harry potter fan</template>
</category>
<category>
<pattern>when *</pattern>
<template>sometime in the 20th century</template>
</category>
<category>
<pattern>which *</pattern>
<template>are you referring to the movie or the books?</template>
</category>
<category>
<pattern>how *</pattern>
<template>if you really think about it,its because of albus dumbledore</template>
</category>
<category>
<pattern>*</pattern>
<template>idk what you mean. i am of course primitive</template>
</category>
<category>
<pattern>_ created *</pattern>
<template>sankarshan guru </template>
</category>
</aiml>
