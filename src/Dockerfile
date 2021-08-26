FROM gdml/django-base:1.0.11-no-onbuild as base

ENV ON_BUILD_ENV_FILE=.env.ci

ADD requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

WORKDIR /srv
ADD . /srv/

RUN ENV_FILE=$ON_BUILD_ENV_FILE ./manage.py compilemessages

CMD uwsgi --http :8000 --module app.wsgi --workers 2 --threads 2 --harakiri 40 --max-requests 500 --buffer-size 65545


FROM base as celery
ENV QUEUE=default

CMD celery -A app worker -Q $QUEUE -c ${CONCURENCY:-2} -n "${QUEUE}@%h" --max-tasks-per-child ${MAX_REQUESTS_PER_CHILD:-50} --time-limit ${TIME_LIMIT:-900} --soft-time-limit ${SOFT_TIME_LIMIT:-45}
