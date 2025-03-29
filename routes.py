from flask import Blueprint, request, jsonify
from models import db, Job

routes = Blueprint('routes', __name__)

# GET all jobs
@routes.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    return jsonify([{'id': job.id, 'title': job.title, 'company': job.company, 'description': job.description, 'location': job.location} for job in jobs])

# POST new job
@routes.route('/jobs', methods=['POST'])
def create_job():
    data = request.json
    new_job = Job(title=data['title'], company=data['company'], description=data['description'], location=data['location'])
    db.session.add(new_job)
    db.session.commit()
    return jsonify({'message': 'Job created successfully'}), 201

# PUT update job
@routes.route('/jobs/<int:job_id>', methods=['PUT'])
def update_job(job_id):
    job = Job.query.get(job_id)
    if not job:
        return jsonify({'error': 'Job not found'}), 404

    data = request.json
    job.title = data.get('title', job.title)
    job.company = data.get('company', job.company)
    job.description = data.get('description', job.description)
    job.location = data.get('location', job.location)

    db.session.commit()
    return jsonify({'message': 'Job updated successfully'}), 200

# DELETE job
@routes.route('/jobs/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    job = Job.query.get(job_id)
    if not job:
        return jsonify({'error': 'Job not found'}), 404

    db.session.delete(job)
    db.session.commit()
    return jsonify({'message': 'Job deleted successfully'}), 200
