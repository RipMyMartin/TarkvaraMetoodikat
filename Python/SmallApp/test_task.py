from task import Task

def test_mark_done():
    task = Task("Testi Ylesanne")
    task.mark_done()
    assert task.status == "done"