# Poetry Search
In this assignment, you will use the PoetryDB API to search for poems by title and/or author. The goal is to write a program that asks the user for an author to search, a poem title to search and then fetches the relevant poems from the PoetryDB API. The program should display how many poems are returned and print the first 5 poems in a user-friendly format.

In Sunrise, you used parameters to define the information you wanted to get from the API. In this assignment, you will use dynamic endpoints which must be constructed in the URL.

The format of the Poetry DB API URL is:
https://poetrydb.org/author,title/{Author to search};{Title to search}
In the above URL, `{Author to search}` and `{Title to search}` are placeholders for the actual author and title you want to search for. You will replace these placeholders with the user input. This is a good potential use for fstrings


You can see an example search for author = "Shakespeare" and title = "Sonnet":
[https://poetrydb.org/author,title/Shakespeare;Sonnet](https://poetrydb.org/author,title/Shakespeare;Sonnet)

The JSON returned by the API will be a list of dictionaries, where each dictionary in the list represents a poem. 

One singular poem dictionary in the list might look like this:
```json
{
    "title": "Sonnet 7: Lo! in the orient when the gracious light",
    "author": "William Shakespeare",
    "lines": [
      "Lo! in the orient when the gracious light",
      "Lifts up his burning head, each under eye",
      "Doth homage to his new-appearing sight,",
      "Serving with looks his sacred majesty;",
      "And having climb'd the steep-up heavenly hill,",
      "Resembling strong youth in his middle age,",
      "Yet mortal looks adore his beauty still,",
      "Attending on his golden pilgrimage:",
      "But when from highmost pitch, with weary car,",
      "Like feeble age, he reeleth from the day,",
      "The eyes, 'fore duteous, now converted are",
      "From his low tract, and look another way:",
      "  So thou, thyself outgoing in thy noon:",
      "  Unlook'd, on diest unless thou get a son."
    ],
    "linecount": "14"
  }
```

An example output should look like this:

```
Enter the author's name: Shakespeare
Enter the poem's title: sonnet
Found 154 poems.

Title: Sonnet 1: From fairest creatures we desire increase
Author: William Shakespeare
Lines:
  From fairest creatures we desire increase,
  That thereby beauty's rose might never die,
  But as the riper should by time decease,
  His tender heir might bear his memory:
  But thou contracted to thine own bright eyes,
  Feed'st thy light's flame with self-substantial fuel,
  Making a famine where abundance lies,
  Thy self thy foe, to thy sweet self too cruel:
  Thou that art now the world's fresh ornament,
  And only herald to the gaudy spring,
  Within thine own bud buriest thy content,
  And tender churl mak'st waste in niggarding:
    Pity the world, or else this glutton be,
    To eat the world's due, by the grave and thee.

Title: Sonnet 2: When forty winters shall besiege thy brow
Author: William Shakespeare
Lines:
  When forty winters shall besiege thy brow,
  And dig deep trenches in thy beauty's field,
  Thy youth's proud livery so gazed on now,
  Will be a tatter'd weed of small worth held:
  Then being asked, where all thy beauty lies,
  Where all the treasure of thy lusty days;
  To say, within thine own deep sunken eyes,
  Were an all-eating shame, and thriftless praise.
  How much more praise deserv'd thy beauty's use,
  If thou couldst answer 'This fair child of mine
  Shall sum my count, and make my old excuse,'
  Proving his beauty by succession thine!
    This were to be new made when thou art old,
    And see thy blood warm when thou feel'st it cold.

Title: Sonnet 3: Look in thy glass and tell the face thou viewest
Author: William Shakespeare
Lines:
  Look in thy glass and tell the face thou viewest
  Now is the time that face should form another;
  Whose fresh repair if now thou not renewest,
  Thou dost beguile the world, unbless some mother.
  For where is she so fair whose unear'd womb
  Disdains the tillage of thy husbandry?
  Or who is he so fond will be the tomb,
  Of his self-love to stop posterity?
  Thou art thy mother's glass and she in thee
  Calls back the lovely April of her prime;
  So thou through windows of thine age shalt see,
  Despite of wrinkles this thy golden time.
    But if thou live, remember'd not to be,
    Die single and thine image dies with thee.

Title: Sonnet 4: Unthrifty loveliness, why dost thou spend
Author: William Shakespeare
Lines:
  Unthrifty loveliness, why dost thou spend
  Upon thy self thy beauty's legacy?
  Nature's bequest gives nothing, but doth lend,
  And being frank she lends to those are free:
  Then, beauteous niggard, why dost thou abuse
  The bounteous largess given thee to give?
  Profitless usurer, why dost thou use
  So great a sum of sums, yet canst not live?
  For having traffic with thy self alone,
  Thou of thy self thy sweet self dost deceive:
  Then how when nature calls thee to be gone,
  What acceptable audit canst thou leave?
    Thy unused beauty must be tombed with thee,
    Which, used, lives th' executor to be.

Title: Sonnet 5: Those hours, that with gentle work did frame
Author: William Shakespeare
Lines:
  Those hours, that with gentle work did frame
  The lovely gaze where every eye doth dwell,
  Will play the tyrants to the very same
  And that unfair which fairly doth excel;
  For never-resting time leads summer on
  To hideous winter, and confounds him there;
  Sap checked with frost, and lusty leaves quite gone,
  Beauty o'er-snowed and bareness every where:
  Then were not summer's distillation left,
  A liquid prisoner pent in walls of glass,
  Beauty's effect with beauty were bereft,
  Nor it, nor no remembrance what it was:
    But flowers distill'd, though they with winter meet,
    Leese but their show; their substance still lives sweet.
```