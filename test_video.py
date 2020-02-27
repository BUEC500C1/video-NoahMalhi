import main
import dev_image
import twitter_fetch
import pytest

#just tests successfull run
def test_twitterpull(testname):

    (tweets, images) = main.main(testname)
    assert images[0] == "ERkrNheVAAAMcIq"
    assert tweets[0] == "This is a pytest test tweet"
    assert tweets[1] == "Seconds test tweet"
    assert tweets[2] == "Thirdd, no image"