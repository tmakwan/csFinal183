/**
 * Created by timmy on 12/10/15.
 */
// populate our app with some sample comments
var sampleComments = [
  { author: 'Rich', text: 'FIRST!!!' },
  { author: 'anonymous', text: 'I disagree with the previous commenter' },
  { author: 'Samuel L. Ipsum', text: "If they don't know, that means we never told anyone. And if we never told anyone it means we never made it back. Hence we die down here. Just as a matter of deductive logic.\n\nYou think water moves fast? You should see ice. It moves like it has a mind. Like it knows it killed the world once and got a taste for murder." },
  { author: 'Jon Grubber', text: '**Hey you guys!** I can use [markdown](http://daringfireball.net/projects/markdown/) in my posts' }
];

var ractive = new CommentWidget({
  el: demo,
  data: {
    comments: sampleComments
  }
});

ractive.on( 'newComment', function ( comment ) {
  console.log( 'saving to server...', comment );
});