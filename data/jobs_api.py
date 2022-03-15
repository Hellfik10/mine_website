import flask
from flask import jsonify, request
from . import db_session
from .jobs import Jobs


blueprint = flask.Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs', methods=["GET"])
def get_news():
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('team_leader', 'collaborators', 'is_finished'))
                 for item in news]
        }
    )


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['GET'])
def get_one_news(jobs_id):
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).get(jobs_id)
    if not news:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'news': news.to_dict()
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['team_leader', 'job', 'work_size', 'is_finished', 'collaborators']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    jobs = Jobs(
        team_leader=request.json['team_leader'],
        job=request.json['job'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        is_finished=request.json['is_finished']
    )
    db_sess.add(jobs)
    db_sess.commit()
    return jsonify({'success': 'OK'})