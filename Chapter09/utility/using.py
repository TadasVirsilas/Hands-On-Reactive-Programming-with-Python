import rx
import rx.operators as ops
from rx.subject import Subject
import datetime
import time
from rx.disposable import Disposable


def resource():
    print("create resource at {}".format(datetime.datetime.now()))

    def dispose():
        print("dispose resource at {}".format(datetime.datetime.now()))

    return Disposable(dispose)


rx.using(resource, lambda r: rx.just(1).pipe(ops.delay(0.2))).subscribe(
    on_next=lambda i: print("on_next {}".format(i)),
    on_error=lambda e: print("on_error: {}".format(e)),
    on_completed=lambda: print("on_completed")
)
time.sleep(500)
