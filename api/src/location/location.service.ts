import { Injectable } from '@nestjs/common';
import { CreateLocationDto } from './dto/create-location.dto';

@Injectable()
export class LocationService {
  create(createLocationDto: CreateLocationDto) {
    return 'This action adds a new location';
  }

  findAll() {
    return `This action returns all location`;
  }

  findOne(id: number) {
    return `This action returns a #${id} location`;
  }

  remove(id: number) {
    return `This action removes a #${id} location`;
  }
}
