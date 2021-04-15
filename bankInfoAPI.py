import bankInfo
from flask import Flask, request
from flask_restful import Resource,Api


app=Flask(__name__)
api=Api(app)

class searchClassAndRow(Resource):
    def get(self):
        para=request.args.get('q')
        limit=request.args.get('limit')
        offset=request.args.get('offset')
        query1 = "select * from bank_branches where ifsc||bank_id||branch||address||city||district||state||bank_name @@ to_tsquery(%s) ORDER BY ifsc ASC LIMIT " + limit + " OFFSET " + offset + ";"
        data = bankInfo.connect(para,query1)
        return {
            'branches':data
               },200


class autocomplete(Resource):
    def get(self):
        para = request.args.get('q')
        limit=request.args.get('limit')
        offset=request.args.get('offset')
        query2="select * from bank_branches where to_tsquery(%s|| ':*') @@ to_tsvector(branch) ORDER BY ifsc ASC LIMIT " + limit + " OFFSET " + offset + ";"
        data = bankInfo.connect(para,query2)
        return {
            'branches':data
               },200



api.add_resource(searchClassAndRow,"/api/branches")
api.add_resource(autocomplete,"/api/branches/autocomplete")


if __name__=='__main__':
    app.run(debug=True)