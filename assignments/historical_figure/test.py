from historical_figure import HistoricalFigure

def test_ada_lovelace():
    ada = HistoricalFigure(
        name="Ada Lovelace",
        field="science",
        quote="That brain of mine is something more than merely mortal, as time will show."
    )

    ada.add_contribution("Wrote the first algorithm")
    ada.add_contribution("Worked with Charles Babbage")

    expected_summary = "Ada Lovelace was a key figure in science. Known for: ['Wrote the first algorithm', 'Worked with Charles Babbage']."
    expected_quote = "Ada Lovelace once said: 'That brain of mine is something more than merely mortal, as time will show.'"

    assert ada.get_summary() == expected_summary, "Ada's summary is incorrect"
    assert ada.share_quote() == expected_quote, "Ada's quote is incorrect"

def test_mlk():
    mlk = HistoricalFigure(
        name="Martin Luther King Jr.",
        field="civil rights",
        quote="Injustice anywhere is a threat to justice everywhere."
    )

    mlk.add_contribution("Led the Montgomery Bus Boycott")
    mlk.add_contribution("Delivered the 'I Have a Dream' speech")

    expected_summary = "Martin Luther King Jr. was a key figure in civil rights. Known for: ['Led the Montgomery Bus Boycott', \"Delivered the 'I Have a Dream' speech\"]."
    expected_quote = "Martin Luther King Jr. once said: 'Injustice anywhere is a threat to justice everywhere.'"

    assert mlk.get_summary() == expected_summary, "MLK's summary is incorrect"
    assert mlk.share_quote() == expected_quote, "MLK's quote is incorrect"

def test_shakespeare():
    shakes = HistoricalFigure(
        name="William Shakespeare",
        field="literature",
        quote="All the world's a stage, and all the men and women merely players."
    )

    shakes.add_contribution("Wrote Hamlet")
    shakes.add_contribution("Popularized the sonnet")
    shakes.add_contribution("Invented over 1,700 words")

    expected_summary = "William Shakespeare was a key figure in literature. Known for: ['Wrote Hamlet', 'Popularized the sonnet', 'Invented over 1,700 words']."
    expected_quote = "William Shakespeare once said: 'All the world's a stage, and all the men and women merely players.'"

    assert shakes.get_summary() == expected_summary, "Shakespeare's summary is incorrect"
    assert shakes.share_quote() == expected_quote, "Shakespeare's quote is incorrect"

def test_no_contributions():
    unknown = HistoricalFigure(
        name="Mystery Person",
        field="unknown",
        quote="No one remembers me... yet."
    )

    expected_summary = "Mystery Person was a key figure in unknown. Known for: []."
    expected_quote = "Mystery Person once said: 'No one remembers me... yet.'"

    assert unknown.get_summary() == expected_summary, "Empty contributions case failed"
    assert unknown.share_quote() == expected_quote, "Quote formatting failed for unknown person"

def run_all_tests():
    test_ada_lovelace()
    test_mlk()
    test_shakespeare()
    test_no_contributions()
    print("All tests passed!")

if __name__ == "__main__":
    run_all_tests()
