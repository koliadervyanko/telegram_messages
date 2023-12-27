import { Injectable, InternalServerErrorException } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { GroupEntity } from './entities/group.entity';
import { Repository } from 'typeorm';

@Injectable()
export class GroupService {
  constructor(
    @InjectRepository(GroupEntity) private repository: Repository<GroupEntity>,
  ) {}
  findAll() {
    try {
      return this.repository.find();
    } catch (error) {
      throw new InternalServerErrorException(`Error ${error}`);
    }
  }
  async findOne(link: string) {
    try {
      const group = await this.repository.findOneBy({ link });
      return group;
    } catch (error) {
      throw new InternalServerErrorException(`Error ${error}`);
    }
  }
}
